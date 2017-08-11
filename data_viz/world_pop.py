import json
from countries import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_pop={}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name=pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_pop[code] = population

#render as svg
wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.force_uri_protocol = 'http'

wm.title = 'World Population, 2010'
wm.add('2010', cc_pop)
wm.render_to_file('world_pop.svg')
