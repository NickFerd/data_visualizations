import pygal
from die_class import Die
from operator import methodcaller, attrgetter

# Create dice instances
die_1 = Die()
die_2 = Die(8)
die_3 = Die(10)
dice = list((die_1, die_2, die_3))

# Make rolls and store the results in a list
results = []
for i in range(75000):
    result = sum(list(map(methodcaller('roll'), dice)))
    results.append(result)

# Analyze the results
max_number = sum(list(map(attrgetter('num_sides'), dice)))
n = len(dice)
frequencies = [0] * (max_number+1)
for res in results:
    frequencies[res] += 1

# Visualize the results
hist = pygal.Bar()
hist.title = 'Results of rolling a D6, D8 and D10 dice 75,000 times'
hist.x_labels = list(range(max_number+1+n))
hist.x_title = "Result"
hist.y_title = 'Frequency of Result'

hist.add('D6 + D8 + D10', frequencies)
hist.render_to_file('D6_D8_D10.svg')

