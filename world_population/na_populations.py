# -*- coding=utf-8 -*-
from pygal.maps.world import World



wm = World()
wm.title = 'Populations of Countries in North America'

# 每一行的国家颜色都是一样的。
wm.add("North America", {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
# 生成file文件
wm.render_to_file('na_populations.svg')