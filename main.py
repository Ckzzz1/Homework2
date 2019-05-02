from collector import *
from data import *
if __name__ == '__main__':      #根据code中的所需数据爬取数据并存入本地数据库中
    data = DATA()
    data.init()
    data.create()

    for name in code.keys():
        dic = get_data(name)
        data.update(name, dic)

    data.save()