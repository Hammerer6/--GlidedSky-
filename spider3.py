import urllib.request
import urllib.parse
import re 
from bs4 import BeautifulSoup
import time
import random
import requests

def main():
    baseurl="http://www.glidedsky.com/level/web/crawler-ip-block-1?page="
    time.sleep(5)  #适当休眠程序
    #askUrl(baseurl)
    #moreUrl(baseurl)
#解析网页的规则
findNum=re.compile(r'<div class="col-md-1">(.*?)</div>',re.S)


#检测ip的可用性
def testIp(proxy):
    headers={"User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"}
    proxies={
    "http":"http://"+proxy,
    "https":"http://"+proxy
    }
    try:
        response=requests.get(url="http://www.ip.cn/",headers=headers,proxies=proxies,timeout=3)
        response.close()
        if response.status_code==200:
            print("可用",proxy)
        else:
            print("不可以")
    except:
        print("ip异常")



#请求网页内容函数，并得到html
def askUrl(url):
    html="" 
    headers={
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36",
    "cookie":"glidedsky_session=eyJpdiI6ImZsSmNBY2lZbmdVa1A0UU5MbzY5OFE9PSIsInZhbHVlIjoidVJ6K0EzRVJwME5HVXhNVXc0enJpcDJJN3VlUlpic2ZPbXhPYXpPMmlmdGNiRWtLZHVIRjJPakNmVmlEcGFWaiIsIm1hYyI6ImEzOGNhNTk3MGI2ZjdlMDZhOTJlYWQzN2VkNWE0MTY2OTkzNWE4NTY3NDFhMDhmYzgzMjE0ZDJjZGU0NWUwN2IifQ=="
    }
    proxy ={"http":"183.173.71.201:10080"}
    httpproxy_handler=urllib.request.ProxyHandler(proxy)  #设置代理请求
    opener=urllib.request.build_opener(httpproxy_handler) #带入代理
    myRequest=urllib.request.Request(headers=headers,url=url)

    #检查错误
    try:
        myResponse=opener.open(myRequest,timeout=4.5) #此处设置超时
        html=myResponse.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


#请求更多网页内容
def moreUrl(baseurl):
    datalist=[]
    for i in range(1,1001):
        url=baseurl+str(i)
        html=askUrl(url) #利用askUrl函数得到html
        # print(html)
        #解析并保存
        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all("div",class_="col-md-1"):
            #print(item) #正确运行
            dataNum=re.findall(findNum,str(item))[0].strip() #此处使用正则表达式时出现TypeError: expected string or bytes-like object的问题，需要将要处理的数据str化
            print(dataNum)  #问题出现，已解决
            datalist.append(int(dataNum))
    return sum(datalist)

#测试函数
if __name__ =="__main__":
    #main()
    testIp("223.215.176.219:8089")
    print("over")
