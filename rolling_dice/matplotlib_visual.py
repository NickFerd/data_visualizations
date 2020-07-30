import matplotlib.pyplot as plt
from die_class import Die
from operator import methodcaller, attrgetter

# Create several dice instances with different number of sides
die_1 = Die()
die_2 = Die(10)
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

# Visualize frequencies with matplotlib.pyplot
plt.figure(figsize=(10, 6))

x = list(range(max_number+1))
hist = plt.bar(x, frequencies)
plt.title("Rolling a D6 and two D10 dice 75,000 times", fontsize=20)
plt.xlabel('Values', fontsize=16)
plt.xticks(x, fontsize=12)

plt.ylabel('Frequency of Value', fontsize=16)
plt.yticks(fontsize=12)

plt.grid(axis='y', linestyle='--', alpha=0.9)

plt.savefig('matplotlib_visualization.png')