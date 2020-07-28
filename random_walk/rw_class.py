from random import choice


def get_next_step(steps_range=5):
    """Calculate the size of a step"""
    direction = choice([-1, 1])
    distance = choice(range(steps_range))
    step = direction * distance
    return step


class RandomWalk:
    """A class to generate random 2D walks"""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk"""
        self.num_points = num_points

        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Generate all points in the walk"""

        # Take steps until the walk reaches desired length
        while len(self.x_values) < self.num_points:

            # Get next step size
            x_step = get_next_step()
            y_step = get_next_step()

            # Reject null moves
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next dot coordinates
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)





