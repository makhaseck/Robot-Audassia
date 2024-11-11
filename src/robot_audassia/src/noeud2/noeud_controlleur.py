#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String

def state_callback(data):
    # Callback pour afficher l'etat du robot
    rospy.loginfo("État du robot : %s", data.data)

def control_node():
    # Initialiser le noeud
    rospy.init_node('noeud_controlleur', anonymous=True)
    
    # Publier un message pour indiquer que le robot avance
    pub = rospy.Publisher("/robot/cmd_vel", Twist, queue_size=10)
    
    # Crer un message Twist pour envoyer la commande de deplacement
    move_msg = Twist()
    move_msg.linear.x = 0.1  # Avance avec une vitesse lineaire positive
    
    # Publier la commande toutes les 1 seconde
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        pub.publish(move_msg)  # Publier la commande
        rospy.loginfo("Envoi de la commande de deplacement.")
        rate.sleep()

    # S'abonner au topic pour recuperer l'etat du robot
    rospy.Subscriber("/robot/state", String, state_callback)
    
    rospy.spin()  # Laisser tourner le noeud

if __name__ == '__main__':
    try:
        control_node()
    except rospy.ROSInterruptException:
        pass

