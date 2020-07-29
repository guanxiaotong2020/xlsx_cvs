
#from urllib.request import Request
import re
from urllib import request, error
from bs4 import BeautifulSoup

def askURL(url):
    head = {"User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 64.0.3282.140 Safari / 537.36Edge / 18.17763"}
    req = request.Request(url, headers = head)
    html = ""
    try:
        response = request.urlopen(req)
        html = response.read().decode(encoding = "utf-8")
    except error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


relink = re.compile(r'<a href="(.*)/">')
rename = re.compile(r'<span class="title">(.*)</span>')

def get_data(url, html):
    datalist = []
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all("div", class_="item"):
        # print(item)
        # print("***********************************************************************************************************************************************************")
        data = []
        item = str(item)
        link = re.findall(relink, item)[0]
        print(link)
        data.append(link)
        name = re.findall(rename, item)
        # if len(name) == 2:
        #     data.extend(name)
        # else:
        #     data.append(name[0])
        #     data.append(" ")
        # print(data)



if __name__ == "__main__":
    baseurl = "https://movie.douban.com/top250?start="
    for i in range(1):
        html = askURL(baseurl + str(i*25))
        print(html)
        get_data(baseurl + str(i*25), html)