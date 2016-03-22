#!/usr/bin/env python

"""This script implements a simple test for the Trajectory objects.
First, a Trajectory object is made.
A ROS node is made, and it publishes the output of the trajectory.
Note that there is no need to define a class for making the ROS node.
"""


import rospy as rp
import geometry_msgs.msg as gm
import trajectories.database as db
import sml_clean.srv as smlsrv


"""Pick the trajectory."""
#TrajectoryType = fptj.FixedPointTrajectory
#TrajectoryType = ctj.CircleTrajectory


"""Pick the parameters from line input.
The GUI can use this feature to let the user define the desired trajectory.
"""
#num_args = TrajectoryType.__init__.__code__.co_argcount
#args_names = TrajectoryType.__init__.__code__.co_varnames[1:num_args]
#print args_names
#args = {}
#for arg_name in args_names:
#    arg = raw_input("Insert " + arg_name + ": ")
#    if arg:
#        args[arg_name] = float(arg)
#my_traj = TrajectoryType(**args)


"""Make the trajectory from a service"""

my_traj = None

def make_trajectory_handler(request):
    TrajectoryType = db.database[request.trajectory_name]
    params = {}
    params["offset"] = request.offset
    params["rotation"] = request.rotation
    for index, name in enumerate(request.parameters_names):
        params[name] = request.parameters_values[index]
    num_args = TrajectoryType.__init__.__code__.co_argcount
    allowed_names = TrajectoryType.__init__.__code__.co_varnames[1:num_args]
    args = {name: value for (name,value) in params.iteritems() if name in allowed_names}
    others = {name: value for (name,value) in params.iteritems() if name not in allowed_names}
    global my_traj
    my_traj = TrajectoryType(**args)
    return True

service = rp.Service('make_trajectory', smlsrv.MakeTrajectory,
    make_trajectory_handler)

    
"""Use the default parameters"""
#args = {}
#my_traj = TrajectoryType(**args)

rp.init_node("trajectory_test_node")
pub = rp.Publisher('position', gm.Point, queue_size=10)
initial_time = rp.get_time()
rate = rp.Rate(30.0)


while not rp.is_shutdown():
    while my_traj == None:
        rate.sleep()
    time = rp.get_time() - initial_time
    pos_msg = list(my_traj.output(time)[0])
    pub.publish(*pos_msg)
    rate.sleep()
    
