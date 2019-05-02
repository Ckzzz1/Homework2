import requests
import time
code = {"年末总人口": '"A030101"', "男性人口": '"A030102"', "女性人口": '"A030103"', "经济活动人口": '"A040101"', "农业总产值": '"A0D0402"', "林业总产值": '"A0D0403"', "牧业总产值": '"A0D0404"', "渔业总产值": '"A0D0405"'}

globals = {
    'true': 0,
    'false': 1
}

def gettime():      # 用来获取 时间戳
    return int(round(time.time() * 1000))


def get_data(parameter):        #爬取数据
    parameter = code[parameter]
    headers = {}
    key = {}
    url = 'http://data.stats.gov.cn/easyquery.htm'

    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'

    key['m'] = 'QueryData'
    key['dbcode'] = 'hgnd'
    key['rowcode'] = 'zb'
    key['colcode'] = 'sj'
    key['wds'] = '[]'
    key['dfwds'] = '[{"wdcode":"zb","valuecode":' + parameter + '}]'
    key['k1'] = str(gettime())

    s = requests.session()
    r = s.get(url, params=key, headers=headers)
    dic = dict(eval(r.text, globals))
    print(dic['returndata']['wdnodes'][0]['nodes'][0]['cname'])
    data = {}
    for i in dic['returndata']['datanodes']:
        data[i['wds'][1]['valuecode']] = i['data']['data']

    for date in range(1999, 2009):
        key['dfwds'] = '[{"wdcode":"sj","valuecode":"' + str(date) + '"}]'
        r = s.get(url, params=key, headers=headers)
        dic = dict(eval(r.text, globals))
        data[dic['returndata']['datanodes'][0]['wds'][1]['valuecode']] = dic['returndata']['datanodes'][0]['data'][
            'data']
    print(data)
    return data
