import json, pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
from get_country_code import get_country_code
# Load the data in the relevant json file

# V1.2 groups population into 3 groups to increase contrast

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    
# Build a population dictionary for 2010
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # We avoid error due to non integral values by
        # converting to a float then dropping the floating
        # decimal places when we make an integer
        # (rounding may be more intuitive next time)
        population = int(float(pop_dict['Value']))
        
        # Since pygal's country mapping codes are in 2-digit format
        # We must convert, we use the get_country_code module we created
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Grouping occurs here
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm_style = RotateStyle('#336699', base_style = LightColorizedStyle)
wm = pygal.maps.world.World(style = wm_style)
wm.title = 'World Population by Country, 2010'
wm.add('0-10 m', cc_pops_1)
wm.add('10 m-1 bn', cc_pops_2)
wm.add('> 1 bn', cc_pops_3)

wm.render_to_file('world_population.svg')


# filename = 'population_data.json'
# with open(filename) as f:
#     pop_data = json.load(f)
    
# # Build a population dictionary for 2010
# cc_populations = {}
# for pop_dict in pop_data:
#     if pop_dict['Year'] == '2010':
#         country_name = pop_dict['Country Name']
#         # We avoid error due to non integral values by
#         # converting to a float then dropping the floating
#         # decimal places when we make an integer
#         # (rounding may be more intuitive next time)
#         population = int(float(pop_dict['Value']))
        
#         # Since pygal's country mapping codes are in 2-digit format
#         # We must convert, we use the get_country_code module we created
#         code = get_country_code(country_name)
#         if code:
#             cc_populations[code] = population

# wm = pygal.maps.world.World()
# wm.title = 'World Population by Country, 2010'
# wm.add('2010', cc_populations)

# wm.render_to_file('world_population.svg')

# # pygal has built in worldmap plot generation
# Example:
# wm = pygal.maps.world.World()
# wm.title = 'Populations of Countries in North America'
# wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

# wm.render_to_file('na_populations.svg')
