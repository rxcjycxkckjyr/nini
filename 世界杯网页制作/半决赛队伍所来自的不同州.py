from pyecharts.charts import Bar
from pyecharts import options as opt


x = [ 'America', 'Europe','Asia']
y1 = [7, 15, 2]
#y2 = [500, 10, 50, 4000, 5000]

mybar = Bar()   # 实例化
mybar.add_xaxis(xaxis_data=x)
mybar.add_yaxis(series_name='州出现频数', y_axis=y1)
#mybar.add_yaxis(series_name='张三', y_axis=y2)
mybar.set_global_opts(title_opts=opt.TitleOpts(title="半决赛队伍所来自不同州"))
mybar.render("半决赛队伍所来自不同州.html")