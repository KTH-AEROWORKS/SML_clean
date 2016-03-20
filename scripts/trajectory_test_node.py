#!/usr/bin/env python

"""This script implements a simple test for the Trajectory objects.
First, a Trajectory object is made.
A ROS node is made, and it publishes the output of the trajectory.
Note that there is no need to define a class for making the ROS node.
"""


import rospy as rp
import geometry_msgs.msg as gm
import trajectories.circle_trajectory as ctj

#args_names = ctj.CircleTrajectory.__init__.__code__.co_varnames[1:]
args = {}
#for arg_name in args_names:
#    arg = raw_input("Insert " + arg_name + ": ")
#    if arg:
#        args[arg_name] = float(arg)
    
my_circle = ctj.CircleTrajectory(**args)

rp.init_node("trajectory_test_node")
pub = rp.Publisher('position', gm.Point, queue_size=10)
initial_time = rp.get_time()
rate = rp.Rate(30.0)


while not rp.is_shutdown():
    time = rp.get_time() - initial_time
    pos_msg = list(my_circle.output(time)[0])
    pub.publish(*pos_msg)
    rate.sleep()
