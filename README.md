# Robot-audassia

Le but de ce projet est de créer un package ROS et ensuite créer trois nœud pour à la fin voir les données d'un lidar SICKLMS100 positionné dans un prototype de robot autonome et même faire la visualisation via rviz et gazebo.
Le package est nommée robot_audassia et j'ai crée noeud dans le repertoire src du package.

## Get started!

### Using Docker 

#### Requirements

- docker
- docker-compose
- be authentified to the docker images registry: https://registry.factory.hotep.team
  - please request a login/password to [Hotep Team](mailto:tech@hotep.team)
  - then you could connect to this docker registry using the following command: `docker login registry.factory.hotep.team` 

#### Prepare development environment

```shell
export PROJECT_HOME=/path/of/my/project

git clone git@github.com/makhaseck/Robot-Audassia ${PROJECT_HOME}
```

#### Start docker-compose

To launch ROS master and nodes:

```shell
cd ${PROJECT_HOME}
docker-compose up 
```

