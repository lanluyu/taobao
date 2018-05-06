# -*- coding:utf-8 -*-

import requests
import re

# 获取网页内容
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()  # 返回状态码异常
        r.encoding = r.apparent_encoding
        return r.text  # 返回的网页内容被赋值给了main()函数中的html
    except:
        return ""

# 解析网页内容
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"price\"\:\"[\d]*\"',html)
        tlt = re.findall(r'\"title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print(' ')

# 打印商品列表
def printGoodList(ilt):
    tplt = '{0:^4}\t{1:^8}\t{2:20}'
    print(tplt.format('序号','价格','手机名称'))
    count = 0
    for g in ilt:
        count = count+1
        print(tplt.format(count,g[0],g[1]))

# 主函数
def main():
    goods = '手机'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s='+str(48*i)  # 此处只取一个url参数，即 &s=
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue  # 获取网页异常是继续程序
    printGoodList(infoList)
main()
