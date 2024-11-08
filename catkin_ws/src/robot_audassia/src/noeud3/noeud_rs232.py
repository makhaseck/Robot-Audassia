#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('noeud_rs232', anonymous=True)
    rospy.loginfo("Demarrage du noeud RS232...")

    command_sub = rospy.Subscriber('/command', String, callback)

    rate = rospy.Rate(2)  # 2 Hz
    while not rospy.is_shutdown():
        rospy.loginfo("En attente de donnees RS232...")
        rate.sleep()

def callback(data):
    rospy.loginfo(f"Commande recues : {data.data}")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

