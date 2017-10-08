# -*- coding=utf-8 -*-
import json
from country_codes_names import get_country_code
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# 读取file的数据
file_name = 'population_data.json'
with open(file_name, 'r', encoding='utf-8') as f:
    pop_data = json.load(f)

# 将地图的数据转换成字典数据{'cn':1338300000}
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        #python不能把带小数点的字符串直接转换成整数，所以要先转换成float
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print('{}:{}'.format(code, str(population)))
            cc_populations[code] = population
        else:
            print('Error-{}'.format(country_name))


# 将所有国家分为三个部分，大于10亿，介于10亿和1000万之间，小于1000万
cc_pops_1,  cc_pops_2, cc_pops_3, = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop > 1000000000:
        cc_pops_1[cc] = pop
    elif pop > 10000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


# 设置pygal的样式
# wm_style = RS('#336699', base_style=LCS)
# wm = World(style=wm_style)
wm = World()
# 设置图表标题
wm.title = 'World Populations in 2010, by Country'
# wm.add('2010', cc_populations)
# 设置分组数据
wm.add('>1bn', cc_pops_1)
wm.add('10m - 1bn', cc_pops_2)
wm.add('<10m', cc_pops_3)
# 生成file
wm.render_to_file('world_populations_groups.svg')