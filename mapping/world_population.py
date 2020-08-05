import pygal
import json
from pygal.style import RotateStyle, BlueStyle
from country_codes import get_country_code


# Extract data from JSON file
filename = 'population_data.json'
with open(filename) as file:
    data = json.load(file)  # list of dict objects

    populations = dict()
    for dict_item in data:
        if dict_item['Year'] == '2010':
            country_name = dict_item['Country Name']
            population = int(float(dict_item['Value']))
            pygal_code = get_country_code(country_name)

            if pygal_code:
                populations[pygal_code] = population


# Group the countries into 4 population levels
pops1, pops2, pops3, pops4 = {}, {}, {}, {}
for code, pop in populations.items():
    if pop < 10000000:
        pops1[code] = pop
    elif pop < 100000000:
        pops2[code] = pop
    elif pop < 300000000:
        pops3[code] = pop
    else:
        pops4[code] = pop


# Visualize countries populations on the Earth map with Pygal
wm_style = RotateStyle('#EF1E0F', step=14, base_style=BlueStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World  Population in 2010, by Country'
#wm.add('0-10m', pops1)
#wm.add('10m-100m', pops2)
wm.add('>300m', pops4)
wm.add('100m-300m', pops3)
wm.add('10m-100m', pops2)
wm.add('0-10m', pops1)


wm.value_formatter = lambda x: "{:,}".format(x)

wm.render_to_file('world_population.svg')