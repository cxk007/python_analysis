# -*- coding=utf-8 -*-
import json


file_name = 'population_data.json'
with open(file_name, 'r', encoding='utf-8') as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        #python不能把带小数点的字符串直接转换成整数，所以要先转换成float
        population = int(float(pop_dict['Value']))
        print('{}:{}'.format(country_name, str(population)))