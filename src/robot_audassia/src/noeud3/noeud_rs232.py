#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def rs232_callback(data):
    # Traitement des donnees venant du topic, par exemple l'etat ou la commande recue
    rospy.loginfo("Commande RS232 recue %s", data.data)

def rs232_node():
    # Initialiser le noeud
    rospy.init_node('noeud_rs232', anonymous=True)
    
    # S'abonner a un topic ou des commandes ou messages sont envoyees
    rospy.Subscriber("/robot/rs232_command", String, rs232_callback)

    # Publier sur un topic d'etat du robot
    pub = rospy.Publisher("/robot/state", String, queue_size=10)
    
    # Exemple d'envoi d'un message d'etat
    pub.publish("Robot pret a recevoir des commandes")
    
    rospy.spin()  # Laisser tourner le noeud

if __name__ == '__main__':
    try:
        rs232_node()
    except rospy.ROSInterruptException:
        pass

