import re
import urllib.request

#url = "https://bit.ly/3rxQFS4"
#html = urllib.request.urlopen(url)
#html_contents = str(html.read())
#id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents)

#for result in id_results:
#   print(result)

#url = "http://www.google.com/googlebooks/uspto-patents-grants-text.html"
#html = urllib.request.urlopen(url)
#html_contents = str(html.read().decode("utf8"))
#url_list = re.findall(r"(http)(.+)(zip)", html_contents)
#for url in url_list:
#    print("".join((url)))

url = "http://finance.naver.com/item/main.nhn?code=005930"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("ms949"))
stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
samsung_stock = stock_results[0] # 두 개 tuple값 중 첫번째 패턴
samsung_index = samsung_stock[1] # 세 개의 tuple값 중 두번째 값
#하나의 괄호가 tuple index가 됨
index_list= re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)", samsung_index)
for index in index_list:
    print(index[1])