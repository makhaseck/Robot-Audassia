#!/usr/bin/env python3
import rospy

def main():
    # Initialise le nœud
    rospy.init_node('noeud_controlleur', anonymous=True)
    rospy.loginfo("Demarrage du noeud de controle...")

    # Boucle principale
    rate = rospy.Rate(2)  # 2 Hz
    count = 0
    while not rospy.is_shutdown():
        # Incremente le compteur
        count += 1

        # Log un message toutes les 5 iterations
        if count % 5 == 0:
            rospy.loginfo("Execution du cycle de controle.")

        # Simuler l'envoi d'une commande
        command = "AVANCER"
        rospy.loginfo(f"Envoi de la commande : {command}")

        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

