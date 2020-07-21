# -*- coding: utf-8 -*-
import sys
import os
import requests
import bs4
import time 
import random 
import csv 
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
#from urllib.parse import quote
sys.path.append("..")

# 输出文件夹路径
out_dirs = 'project\\自用数据\\全国行政区划1.csv'
out_dirs1 = 'project\\自用数据\\全国行政区划_市.csv'
out_dirs2 = 'project\\自用数据\\全国行政区划_区县.csv'
out_dirs3 = 'project\\自用数据\\全国行政区划_乡镇.csv'
out_dirs4 = 'project\\自用数据\\全国行政区划_村.csv'
baseUrl = 'https://xingzhengquhua.51240.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}

proxy_list= ['58.218.92.149:9434','58.218.200.223:2363','183.165.192.196:4245']
proxy = random.choice(proxy_list)
print("当前IP为:",proxy)
proxies = {
'http': 'http://' + proxy,
'https': 'https://' + proxy,
}

# 打印信息
def log(arr):
    if type(arr) is list:
        info = ' '.join(str(v) for v in arr)
    else:
        info = str(arr)
    print(info)
    
def read_csv(url):
    # 读取csv
    csv_data = csv.reader(open(url,'r',encoding='utf-8'))
    return csv_data

def write_csv(path, data, way):
    # 按传入方式 way 写入csv
    if ["a+", "w+", 'r+'].__contains__(way) is False:
        log(['当前传入方式错误：', way])
        sys.exit()

    if type(data) is list:
        data = ','.join(str(v) for v in data)
    elif type(data) is tuple:
        data = ','.join(str(v) for v in data)
    else:
        data = str(data)
    f = open(path, way,encoding='utf-8')
    f.write(data + '\n')
    f.close()


#省
def getQuanGuoCityUrl():
    urllist1 = []
    response = requests.get(baseUrl,headers=headers,proxies=proxies).content.decode("utf-8")
    soup = BeautifulSoup(response,'html.parser')
    result = soup.find('div',class_='kuang')
    time.sleep(1)
    try:
        level1 = result.find_all('tr')
        for level2 in level1[3:]:
            level3 = level2.find_all('td')
            
            city = level3[0].a.string
            code = level3[1].a.string
            # write_csv(out_dirs,["省","行政区划"],'a+')
            write_csv(out_dirs,[city,code],'a+')
            urllist1.append([city,code])
    except:
        pass
    print("省：",urllist1)
    return urllist1
'''
[['北京市', '110000000000'], ['天津市', '120000000000'], ['河北省', '130000000000'], ['山西省', '140000000000'], ['内蒙古自治区', '150000000000'], ['辽宁省', '210000000000'], ['吉林省', '220000000000'], ['黑龙江省', '230000000000'], ['上海市', '310000000000'], ['江 
苏省', '320000000000'], ['浙江省', '330000000000'], ['安徽省', '340000000000'], ['福建省', '350000000000'], ['江西省', '360000000000'], ['山东省', '370000000000'], ['河南省', '410000000000'], ['湖北省', '420000000000'], ['湖南省', '430000000000'], ['广东省', '440000000000'], ['广西壮族自治区', '450000000000'], ['海南省', '460000000000'], ['重庆市', '500000000000'], ['四川省', '510000000000'], [' 
贵州省', '520000000000'], ['云南省', '530000000000'], ['西藏自治区', '540000000000'], ['陕西省', '610000000000'], ['甘肃省', '620000000000'], ['青海省', '630000000000'], ['宁夏回族自治区', '640000000000'], ['新疆维吾尔自治区', '650000000000']]
'''

#市
def getCityUrl():
    urllist2 = []
    # for city in getQuanGuoCityUrl():
    data = read_csv('project\\自用数据\\全国行政区划_省.csv')
    for city in data:
        # print(city)
        url = 'https://xingzhengquhua.51240.com/' + str(city[1]) + '__xingzhengquhua/'
        response1 = requests.get(url,headers=headers,proxies=proxies).content.decode('utf-8')
        soup1 = BeautifulSoup(response1,'html.parser')
        result = soup1.find('div',class_='kuang')
        time.sleep(1)

        level = result.find_all('tr')
        # print(level)
        # if isinstance(level,bs4.element.Tag):
        for level1 in level[3:]:
            level2 = level1.find_all('td')
            try:
                city2 = level2[0].a.string
                code2 = level2[1].a.string
                # print(city2,code2)
                # write_csv(out_dirs,["市","行政区划"],'a+')
                write_csv(out_dirs1,[city2,code2],'a+')
                urllist2.append(code2)
            except:
                print("下一个")
    print("市:",urllist2)
    return urllist2
'''
[['石家庄市', '130100000000'], ['唐山市', '130200000000'], ['秦皇岛市', '130300000000'], ['邯郸市', '130400000000'], ['邢台市', '130500000000'], ['保定市', '130600000000'], ['张家口市', '130700000000'], ['承德市', '130800000000'], ['沧州市', '130900000000'], ['廊坊 
市', '131000000000'], ['衡水市', '131100000000']]
'''


#区
def getQX():
    urllist3 = []
    data = read_csv('project\\自用数据\\全国行政区划_市.csv')
    for qu in data:
        url = 'https://xingzhengquhua.51240.com/' + str(qu[1]) + '__xingzhengquhua/'
        response2 = requests.get(url,headers=headers,proxies=proxies).content.decode('utf-8')
        soup2 = BeautifulSoup(response2,'html.parser')
        result = soup2.find('div',class_='kuang')
        # time.sleep(3)
        if isinstance(result,bs4.element.Tag):
            level = result.find_all('tr')
            for level1 in level[3:]:
                try:
                    level2 = level1.find_all('td')
                    city2 = level2[0].a.string
                    code2 = level2[1].a.string
                    # write_csv(out_dirs,["区县","行政区划"],'a+')
                    write_csv(out_dirs2,[city2,code2],'a+')
                    urllist3.append(code2)
                except:
                    print("下一个")
    print("区：",urllist3)
    return urllist3
'''
[['市辖区', '330701000000'], ['婺城区', '330702000000'], ['金东区', '330703000000'], ['武义县', '330723000000'], ['浦江县', '330726000000'], ['磐安县', '330727000000'], ['兰溪市', '330781000000'], ['义乌市', '330782000000'], ['东阳市', '330783000000'], ['永康市', '330784000000']]
'''

#乡镇
def getXiangZhen():
    urllist4 = []
    data = read_csv('project\\自用数据\\全国行政区划_区县.csv')
    for xiangzhen in data:
        url = 'https://xingzhengquhua.51240.com/' + str(xiangzhen[1]) + '__xingzhengquhua/'
        response3 = requests.get(url,headers=headers,proxies=proxies).content.decode('utf-8')
        soup3 = BeautifulSoup(response3,'html.parser')
        result = soup3.find('div',class_='kuang')
        # time.sleep(1)
        if isinstance(result,bs4.element.Tag):
            level = result.find_all('tr')
            for level1 in level[3:]:
                try:
                    level2 = level1.find_all('td')
                    
                    city2 = level2[0].a.string
                    code2 = level2[1].a.string
                    # write_csv(out_dirs,["乡镇","行政区划"],'a+')
                    write_csv(out_dirs3,[city2,code2],'a+')
                    urllist4.append(code2)
                except:
                    print("下一个")
    print("乡镇:",urllist4)
    return urllist4

'''
[['多湖街道', '330703001000'], ['东孝街道', '330703002000'], ['孝顺镇', '330703101000'], ['傅村镇', '330703102000'], ['曹宅镇', '330703103000'], ['澧浦镇', '330703104000'], ['岭下镇', '330703105000'], ['江东镇', '330703106000'], ['塘雅镇', '330703107000'], ['赤松镇', '330703108000'], ['源东乡', '330703200000']]
'''

#村
def getCun():
    # urllist5 = []
    data = read_csv('project\\自用数据\\全国行政区划_乡镇.csv')
    for cun in data:
        url = 'https://xingzhengquhua.51240.com/' + str(cun[1]) + '__xingzhengquhua/'
        response4 = requests.get(url,headers=headers,proxies=proxies).content.decode('utf-8')
        soup4 = BeautifulSoup(response4,'html.parser')
        result = soup4.find('div',class_='kuang')
        time.sleep(1)
        if isinstance(result,bs4.element.Tag):
            level = result.find_all('tr')
            for level1 in level[3:]:
                try:
                    level2 = level1.find_all('td')
                    
                    city2 = level2[0].a.string
                    code2 = level2[1].a.string
                    fenlei = level2[2].string
                    # urllist4.append([city2,code2,fenlei])
                    print(city2,code2,fenlei)
                    # write_csv(out_dirs,["村","行政区划","城乡分类"],'a+')
                    write_csv(out_dirs4,[city2,code2,fenlei],'a+')
                except:
                    print("下一个")
                
if __name__ == "__main__":
    
    # getQuanGuoCityUrl()
    # getCityUrl()
    # getQX()
    # getXiangZhen()
    getCun()