from plot import *
from data import *

plt=plot()
db=DATA()
db.init()

db.select("年末总人口")  #表一
plt.rect(db.selection,"年末总人口(万人)")

name_list=["男性人口","女性人口"]   #表二
data_list=[]
for name in name_list:
    db.select(name)
    data_list.append(db.selection)
plt.line(data_list,name_list,"性别人口(万人)")

db.select("经济活动人口") #表三
plt.rect(db.selection,"经济活动人口(万人)")

name_list=["农业总产值", "林业总产值", "牧业总产值", "渔业总产值"]  #表四
data_list=[]
for name in name_list:
    db.select(name)
    data_list.append(db.selection[2017])
plt.pie(name_list,data_list,"2017年农林牧渔业比例分布")

