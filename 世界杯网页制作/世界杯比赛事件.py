from pyecharts.charts import Bar
from pyecharts import options as opt


x = ['进球数','黄牌','红牌']
y1 = [2548, 2164, 148]


mybar = Bar()   # 实例化
mybar.add_xaxis(xaxis_data=x)
mybar.add_yaxis(series_name='世界杯比赛事件',y_axis=y1)
mybar.set_global_opts(title_opts=opt.TitleOpts(title="世界杯比赛事件进球、红/黄牌等"))
mybar.render("世界杯比赛事件进球红黄牌等.html")
