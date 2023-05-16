from pyecharts.charts import Bar
from pyecharts import options as opt
import pandas as pd
import numpy as np

data= pd.read_csv("WorldCupsSummary.csv")
#data = data.replace(['Germany FR'],'Germany')

tmp = data['WinnerContinent'].tolist()
tmp_set = set(tmp)
tmp_set = [t for t in tmp_set]
y = np.zeros(len(tmp_set))
x = []
for i in range(len(tmp_set)):
    idx = 0
    x.append(tmp_set[i])
    for j in range(len(tmp)):
        if tmp_set[i] == tmp[j]:
            idx += 1
    y[i] = idx

# print(x)
# print(y)
x = [xx for xx in x]
y = [yy for yy in y]
Bar=Bar()
Bar.add_xaxis(xaxis_data=x)
Bar.add_yaxis(series_name='州出现的频数',y_axis=y)
Bar.set_global_opts(title_opts=opt.TitleOpts(title='冠军所在不同州'))
Bar.render("冠军所在不同的州.html")
