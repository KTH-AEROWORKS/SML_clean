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

database = {}
database[at.Trajectory.description()] = at.Trajectory
database[fpt.FixedPointTrajectory.description()] = fpt.FixedPointTrajectory
database[ct.CircleTrajectory.description()] = ct.CircleTrajectory
