import matplotlib.pyplot as plt
from rw_class import RandomWalk


# Make a random walk, and plot the points
rw = RandomWalk(55000)
rw.fill_walk()

# Set the size of the plotting window
plt.figure(figsize=(10, 6))

# Use a colormap, light-colored  --> dark-colored
point_numbers = list(range(rw.num_points))
points = plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
            cmap=plt.cm.Blues, s=1)

plt.title('2D Random walk (55,000 steps)')

# Emphasize the first and last points
start = plt.scatter(0, 0, c='green', s=25)
finish = plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=25)

# Adding legend
plt.legend((start, finish),
                ('Starting point', 'Finish point'))

plt.savefig('rw_matplotlib.png')




