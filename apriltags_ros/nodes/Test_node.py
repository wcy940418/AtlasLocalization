#!/usr/bin/env python
import roslib
roslib.load_manifest('apriltags_ros')
import rospy
import math
import tf
import geometry_msgs.msg
from std_msgs.msg import String

if __name__== '__main__':
	rospy.init_node('Test_Node')
	listener = tf.TransformListener()  
	publisher = rospy.Publisher('test_output',String, queue_size=1)
	rate = rospy.Rate(10.0)
	init_time=rospy.get_time()
	trans=None
	prev=None
	while not rospy.is_shutdown():
		try:
			#origin 0,0,0 is set to tag_0
			#replace tag_2 with usb_cam to get camera position with respect to origin
			(trans,rot) = listener.lookupTransform('/tag_2', '/tag_0', rospy.Time(0))
		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
			rospy.loginfo("error")
			continue
		if trans != prev:
			out1="Position: %s Rotation: %s" %(trans,tf.transformations.euler_from_quaternion(rot))
			rospy.loginfo(out1)
			publisher.publish(out1)
			rate.sleep()
		prev=trans



