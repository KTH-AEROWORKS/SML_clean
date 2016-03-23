"""This is the database of the trajectories.
It it used by the service MakeTrajectory to make the right type of trajectory
given its name.
When you make a new type of Trajectory,
do not forget to add it to this database,
or the service MakeTrajectory will not be aware of its existence.
"""

import trajectories.trajectory as at
import trajectories.fixed_point_trajectory as fpt
import trajectories.circle_trajectory as ct

trajectories_dictionary = {}
trajectories_dictionary[at.Trajectory.description()] = at.Trajectory
trajectories_dictionary[fpt.FixedPointTrajectory.description()] = fpt.FixedPointTrajectory
trajectories_dictionary[ct.CircleTrajectory.description()] = ct.CircleTrajectory
