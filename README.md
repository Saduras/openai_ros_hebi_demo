# Setup

## Clone openai_ros 
```
git clone https://bitbucket.org/theconstructcore/openai_ros.git
cd openai_ros
git checkout version2
```

## Build catkin workspace
```
catkin build
source ~/catkin_ws/devel/setup.bash
```

## Install openai_ros' python depedencies
```
pip install gym GitPython
```

# Run

```
roslaunch openai_ros_hebi_demo agent.launch
```