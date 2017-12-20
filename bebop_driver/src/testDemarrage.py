#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty

def starter():
    pub = rospy.Publisher('drone1/takeoff', Empty, queue_size = 10)
    pub2 = rospy.Publisher('drone2/takeoff', Empty,  queue_size = 10)
    rospy.init_node('bebop_driver', anonymous=True)
    rate = rospy.Rate(1)
    
    rospy.loginfo('Drones should takeoff')
    pub.publish()
    pub2.publish()

if __name__ == '__main__':
    try:
        starter()
    except rospy.ROSInterruptException:
        pass

