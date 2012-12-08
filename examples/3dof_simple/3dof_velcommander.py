#!/usr/bin/python

import roslib
roslib.load_manifest('ipa_canopen_tutorials')
import rospy
import copy
from cob_srvs.srv import Trigger
from brics_actuator.msg import JointVelocities
from brics_actuator.msg import JointValue

rospy.init_node("ipa_canopen_test")

rospy.wait_for_service('/tray_controller/init')
print "found init"
initService = rospy.ServiceProxy('/tray_controller/init', Trigger)
resp = initService()

velPublisher = rospy.Publisher('/tray_controller/command_vel', JointVelocities)
rospy.sleep(2.0)
v = JointVelocities()
vv1 = JointValue()
vv1.timeStamp = rospy.Time.now()
vv1.joint_uri = "tray_1_joint"
vv2 = copy.deepcopy(vv1)
vv2.joint_uri = "tray_2_joint"
vv3 = copy.deepcopy(vv1)
vv3.joint_uri = "tray_3_joint"
v.velocities = [vv1,vv2,vv3]

v.velocities[0].value = 0.0

while not rospy.is_shutdown():
    v.velocities[0].value = 0.05
    v.velocities[1].value = 0.05
    velPublisher.publish(v)

    rospy.sleep(1.0)

    v.velocities[0].value = 0
    v.velocities[1].value = 0
    velPublisher.publish(v)

    rospy.sleep(1.0)

    v.velocities[0].value = - 0.05
    v.velocities[1].value = - 0.05
    velPublisher.publish(v)

    rospy.sleep(1.0)

    v.velocities[0].value = 0
    v.velocities[1].value = 0
    velPublisher.publish(v)

    rospy.sleep(1.0)
