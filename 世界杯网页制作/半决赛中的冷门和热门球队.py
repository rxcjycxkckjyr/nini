from pyecharts.charts import Bar
from pyecharts import options as opt


x = [ '冷门：Austria、Belgium、Bulgaria、Chile、Croatia、Czechoslovakia、Hungary、Korea Republic、Poland、Portugal、Soviet Union、Spain、Turkey、USA、Yugoslavia',
      '热门：Italy、Uruguay、Germany、Brazil、Argentina、France、England、Sweden、Netherlands、Argentina']
y1 = [14, 10]
#y2 = [500, 10, 50, 4000, 5000]

mybar = Bar()   # 实例化
mybar.add_xaxis(xaxis_data=x)
mybar.add_yaxis(series_name='队伍出现频数', y_axis=y1)
#mybar.add_yaxis(series_name='张三', y_axis=y2)
mybar.set_global_opts(title_opts=opt.TitleOpts(title="半决赛中的冷门和热门"))
mybar.render("半决赛中的冷门和热门.html")