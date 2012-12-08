#!/usr/bin/python

import roslib
roslib.load_manifest('ipa_canopen_tutorials')
import rospy
import actionlib
import control_msgs.msg
import trajectory_msgs.msg
from cob_srvs.srv import Trigger
from brics_actuator.msg import JointVelocities
from brics_actuator.msg import JointValue


#from cob_srvs.srv import Trigger
#from brics_actuator.msg import JointVelocities
#from brics_actuator.msg import JointValue

rospy.init_node("trajectory_controller_action_client")

rospy.wait_for_service('/tray_controller/init')
print "found init"
initService = rospy.ServiceProxy('/tray_controller/init', Trigger)
print "hO"
resp = initService()
print "hI"
print resp

client = actionlib.SimpleActionClient('/tray_controller/follow_joint_trajectory',
                                      control_msgs.msg.FollowJointTrajectoryAction)
client.wait_for_server()

goal = control_msgs.msg.FollowJointTrajectoryGoal()


p = trajectory_msgs.msg.JointTrajectoryPoint()
p.positions = [0.0,0.0,0.5]
p.time_from_start = rospy.Duration(3.0)

goal.trajectory.points = [p]
goal.trajectory.joint_names = ["tray_1_joint","tray_2_joint","tray_3_joint"]
print "hi"

client.send_goal(goal)
client.wait_for_result(rospy.Duration.from_sec(5.0))

print "ok."


