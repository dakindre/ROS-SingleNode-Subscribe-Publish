#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

pub = rospy.Publisher('sum', Int16, queue_size=10)

def callback(data):
	publish(data)

def publish(data):
	sum2 = (data.a + data.b)
	pub.publish(sum2)
    
def main():


    rospy.init_node('solution', anonymous=True)

    rospy.Subscriber("two_ints", TwoInts, callback)

    rospy.spin()


if __name__ == '__main__':
    main()


