#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def lidar_callback(data):
    rospy.loginfo("Donnees du lidar : %s", data.ranges)

def move_callback(data):
    # traitement des commandes de deplacement
    rospy.loginfo("Commande de deplacement recue : %s", data)

def lidar_node():
    # Initialiser le noeud
    rospy.init_node('noeud_lidar', anonymous=True)
    
    # S'abonner au topic "scan" (donnees lidar)
    rospy.Subscriber("/robot/lidar/scan", LaserScan, lidar_callback)
    
    # S'abonner au topic de commande du robot
    rospy.Subscriber("/robot/cmd_vel", Twist, move_callback)

    rospy.spin()  # Laisser tourner le noeud

if __name__ == '__main__':
    try:
        lidar_node()
    except rospy.ROSInterruptException:
        pass

