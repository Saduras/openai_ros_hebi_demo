#!/usr/bin/env python

import numpy as np
import rospkg
import gym

import rospy
from openai_ros.openai_ros_common import StartOpenAI_ROS_Environment
import openai_ros_hebi_demo

if __name__ == '__main__':

    # Initialize the learner as a ROS node
    rospy.init_node('gym_agent', anonymous=True, log_level=rospy.WARN)

    rospy.set_param('/hebi/ros_ws_abspath', '/home/david/catkin_ws/')

    env_name = 'HebiReach-v0'
    gym.register(
        id=env_name,
        entry_point='openai_ros_hebi_demo.task_envs.hebi_reach:HebiReachEnv',
        max_episode_steps=10000,
    )

    env = gym.make(env_name)

    env.reset()
    
    rospy.spin()

    # env.close()
    # rospy.signal_shutdown("End of episodes!")

