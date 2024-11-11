# Robot-audassia
Ce projet vise à développer un prototype virtuel de robot autonome avec un lidar 2D SICK LMS100 et un contrôleur roboteq MD2230. Le tout est simulé dans un environnement virtuel utilisant Gazebo et RViz. Les données des capteurs et les commandes sont échangées via des nœuds ROS, et la communication est établie à travers une connexion Ethernet pour le lidar et une liaison RS232 via Ethernet pour le contrôleur.
Prérequis :
ROS (Noetic, la version compatible avec Ubuntu 20.04)
Gazebo et RViz
Docker et VcXsrv (si vous utilisez un conteneur Docker pour exécuter ROS sur Windows)
Git pour cloner le dépôt
Installation :
Commencez par cloner ce dépôt dans votre répertoire de travail :
git clone https://github.com/makhaseck/Robot-Audassia.git
cd Robot-Audassia
Créez un espace de travail catkin_ws et compilez-le pour ajouter le package robot_audassia:
# Créer l'espace de travail
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src

# Cloner le dépôt dans l'espace de travail
git clone https://github.com/makhaseck/Robot-Audassia.git robot_audassia

# Retourner au répertoire de l'espace de travail et compiler
cd ~/catkin_ws
catkin_make

# Sourcer l'espace de travail
source devel/setup.bash
Lancer les Simulations avec Gazebo et RViz :
roslaunch robot_audassia gazebo_launch.launch
Remarque: Pour éviter d'avoir tous les messages de log dans un même terminal, vous pouvez lancer Gazebo et RViz dans des terminaux séparés.
Nœuds ROS :
Voici un récapitulatif des nœuds utilisés dans le package robot_audassia, avec les commandes pour les exécuter individuellement:
1. Nœud noeud_lidar.py
Ce nœud récupère les données du lidar SICK LMS100. Pour l'exécuter :
rosrun robot_audassia noeud_lidar.py
2. Nœud noeud_controlleur.py
Ce nœud permet de communiquer avec le contrôleur roboteq MD2230. Pour l'exécuter :
rosrun robot_audassia noeud_controlleur.py
3. Nœud noeudrs232.py
Ce nœud gère la liaison série RS232 pour la communication via Ethernet. Pour l'exécuter :
rosrun robot_audassia noeudrs232.py


Auteurs
Ce projet a été développé par makhaseck.

