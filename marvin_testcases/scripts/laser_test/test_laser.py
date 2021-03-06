#!/usr/bin/env python
import unittest
import rospy
from time import sleep
import rostest
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import unittest

class TestLaserscan(unittest.TestCase):

    def callback(self,msg):
        print msg.ranges[270]
        self.r=msg.ranges[270]



    def test_Laserscan(self):
        rospy.init_node('laserscan_test')
        rospy.Subscriber('/scan/front/raw', LaserScan, self.callback)

        counter=0

        while not rospy.is_shutdown() and counter<5:
            sleep(1)
            counter +=1
        self.assertGreaterEqual(round(self.r,1),3.8)



if __name__ == '__main__':
    rostest.rosrun('marvin_testcases','laserscan_test', TestLaserscan)
