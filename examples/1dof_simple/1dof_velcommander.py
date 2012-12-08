#!/usr/bin/python

import roslib
roslib.load_manifest('ipa_canopen_tutorials')
import rospy
from cob_srvs.srv import Trigger
from brics_actuator.msg import JointVelocities
from brics_actuator.msg import JointValue

rospy.init_node("ipa_canopen_test")


rospy.wait_for_service('/mockarm_controller/init')
initService = rospy.ServiceProxy('/mockarm_controller/init', Trigger)
resp = initService()
print resp

velPublisher = rospy.Publisher('/mockarm_controller/command_vel', JointVelocities)
rospy.sleep(2.0)
v = JointVelocities()
vv = JointValue()
vv.timeStamp = rospy.Time.now()
vv.joint_uri = "mockarm_1_joint"
v.velocities = [vv]

while not rospy.is_shutdown():
    v.velocities[0].value = 0.2
    velPublisher.publish(v)

    rospy.sleep(1.0)

    v.velocities[0].value = 0
    velPublisher.publish(v)

    rospy.sleep(1.0)

    v.velocities[0].value = - 0.2
    velPublisher.publish(v)

    rospy.sleep(1.0)
    
    v.velocities[0].value = 0
    velPublisher.publish(v)

    rospy.sleep(1.0)
