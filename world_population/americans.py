# -*- coding=utf-8 -*-
from pygal.maps.world import World


wm = World()
wm.title = 'North, Central, and South America'

# 每一行的国家颜色都是一样的。
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('Sourth America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py','sr', 'uy', 've'])

wm.render_to_file('americas.svg')