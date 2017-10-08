# -*- coding=utf-8 -*-
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 使用api接口获取github上面的数据，你可以看看其他语言的情况，比如改成ruby
url = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)


# 存储API数据到变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 研究仓库有关的信息
repo_dicts = response_dict['items']

# 将项目和stars转换成lists
names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    # Get the project description, if one is available.
    description = repo_dict['description']
    if not description:
        description = "No description provided."

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)

# 将项目可视化.
# 设置pygal样式
my_style = LS('#333366', base_style=LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_label_font_size = 18
# 设置图表样式
my_config = pygal.Config()
# x轴旋转45度
my_config.x_label_rotation = 45
# 隐藏图例
my_config.show_legend = False
# 将名字较长的标签截短成15个
my_config.truncate_label = 15
# 隐藏图表的水平线
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred ruby Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('ruby_repos.svg')