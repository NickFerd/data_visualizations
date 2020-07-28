import pygal
from rw_class import RandomWalk


# Make a random walk instance and plot the points
rw = RandomWalk(10000)
rw.fill_walk()

# List to store values
values = list(zip(rw.x_values, rw.y_values))

# Visualize data with pygal
rw_xy = pygal.XY(stroke=False, dots_size=2)
rw_xy.title = '2D Random walk (10,000 steps)'
rw_xy.add('Steps dots', values)
rw_xy.add('Starting point', (0, 0), dots_size=5)
rw_xy.add('Finish point', [values[-1]], dots_size=5)
rw_xy.render_to_file('rw_pygal.svg')