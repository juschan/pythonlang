from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'

wm.title = 'Population of Countries in North America'

wm.add('North America', {'ca': 34126000, 'mx': 113423000, 'us':309349000})
wm.render_to_file('na_pop.svg')
