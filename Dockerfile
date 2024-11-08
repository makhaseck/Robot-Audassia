FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

COPY [".ops/adds/", "/"]

RUN apt update \
    && apt install -y git curl gnupg lsb-release build-essential vim \
    && curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add - \
    &&  sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list' \
    && apt update \ 
    && apt install -yq ros-noetic-ros-base ros-noetic-ros-core ros-base \ 
    && chmod +x /opt/entrypoint.sh \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

#ENTRYPOINT ["/opt/entrypoint.sh"]
ENTRYPOINT ["bash", "-i", "/opt/entrypoint.sh"]

WORKDIR "/root/catkin_ws"


# dans /root/catkin_ws/src catkin_create_pkg audassia rospy std_msgs sensor_msgs


