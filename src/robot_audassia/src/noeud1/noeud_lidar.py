#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan

def lidar_node():
    rospy.init_node('noeud_lidar', anonymous=True)
    pub = rospy.Publisher('/scan', LaserScan, queue_size=10)
    rate = rospy.Rate(2)  # 2 Hz

    while not rospy.is_shutdown():
        # Crer un message LaserScan avec des donnees fictives pour le test
        msg = LaserScan()
        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "lidar_frame"
        msg.angle_min = -1.57
        msg.angle_max = 1.57
        msg.angle_increment = 0.01
        msg.range_min = 0.1
        msg.range_max = 10.0
        msg.ranges = [1.0] * 314  # 314 echantillons a 1 m
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        lidar_node()
    except rospy.ROSInterruptException:
        pass

