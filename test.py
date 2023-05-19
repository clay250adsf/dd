from bs4 import BeautifulSoup
import requests
url = 'https://www.dy2018.com/e/search/index.php'
mv_list=[]
mv_more_list=[]
mv_load=[]
data = "黑暗荣耀"
req_data = {
    'show': 'title',
    'tempid': '1',
    'keyboard': data.encode('gb2312'),
    'submit': '%C1%A2%BC%B4%CB%D1%CB%F7'
}
# print(req_data)
req = requests.post(url,data=req_data)
soup = BeautifulSoup(req.content,'html.parser',from_encoding='gbk')
result_list = soup.select('div.co_content8 ul')
with open ("result.txt","a+",encoding='utf-8') as f:
    f.write(str(result_list))
    f.close()

for result in result_list:
    result_list_count = len(result.select('a'))
    for i in range (result_list_count): #循环获取页面视频名称，暂时完成，多页面待开发
        movie_name = result.select('a')[i].text
        mv_list.append(movie_name)
        i+=1
    for b in range (result_list_count):
        detail_link = 'http://www.dy2018.com' + result.select('a')[b]['href']
        mv_more_list.append(detail_link)#获取视频详细页面链接

        detail_response = requests.get(detail_link)
        detail_soup = BeautifulSoup(detail_response.content, 'html.parser',from_encoding='gbk')
        # print(len(detail_soup.select('div#downlist table td a')))
        print((len(detail_soup.select('div#downlist table td a'))))
        for c in range(len(detail_soup.select('div#Zoom a'))):
            download_link = detail_soup.select('div#Zoom a')[c]['href']
            mv_load.append(download_link)#获取视频下载链接
            c+=1
        b += 1
print(mv_list)
print(mv_more_list)
print(mv_load)
