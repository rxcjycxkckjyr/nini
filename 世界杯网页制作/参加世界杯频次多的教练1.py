from pyecharts.charts import Line
from pyecharts import options as opt
import pandas as pd


Summary = pd.read_csv("WorldCupPlayers.csv")
x = Summary['Year'].tolist()
x = [str(xx) for xx in x]
y = Summary['Coach Name'].tolist()

myline = Line()   # 实例化
myline.add_xaxis(xaxis_data=x)
myline.add_yaxis(series_name='教练名字', y_axis=y)
myline.set_global_opts(title_opts=opt.TitleOpts(title="参赛队伍数变化趋势"))
myline.render("参赛队伍数变化趋势.html")
