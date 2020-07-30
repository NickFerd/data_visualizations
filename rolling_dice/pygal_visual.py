import pygal
from die_class import Die


# Create two D6 dice
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results
max_number = die_1.num_sides + die_2.num_sides
frequencies = [0] * (max_number+1)
for res in results:
    frequencies[res] += 1

# Visualize the results
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and D10 dice 50,000 times"
hist.x_labels = list(range(max_number+3))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('D6_D10.svg')

