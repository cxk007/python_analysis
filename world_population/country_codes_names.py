# -*- coding=utf-8 -*-
from pygal_maps_world.i18n import COUNTRIES
"""
根据指定的国家名字，返回两个字母的国别码，或者相反。"""

def get_country_code(country_name):
    """
    根据指定国家，返回两个字母的国别码
    :param country_name:
    :return: 返回两个字母的国别码
    """
    for code, name in COUNTRIES.items():
        if name.upper() == country_name.upper():
            return code
    else:
        print('No match found')
        return

def get_country_name(country_code):
    """
    根据国家两位代码来回推国家的名字
    :param country_code:
    :return:
    """
    for code, name in COUNTRIES.items():
        if code.upper() == country_code.upper():
            return name
    else:
        print('No match found')
        return

if __name__ == '__main__':
    print(get_country_code('China'))
    print(get_country_code('United States'))
    print(get_country_code('Chile'))
    # print(get_country_name('us'))
