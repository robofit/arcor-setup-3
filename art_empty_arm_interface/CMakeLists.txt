cmake_minimum_required(VERSION 2.8.3)
project(art_empty_arm_interface)

find_package(catkin REQUIRED COMPONENTS
  art_brain
  rospy
)

catkin_python_setup()

catkin_package()