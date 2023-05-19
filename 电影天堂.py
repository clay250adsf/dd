#encoding='gb2312'
import requests
import lxml
import re
import time,os
from bs4 import BeautifulSoup
from selenium import webdriver as wd
from cookie import * #cookie.py文件引入模块


def Website():
    # web = requests.get("https://www.dy2018.com/e/search/index.php",headers=headers,cookies=cookie)
    # print(web.content.decode('gbk'))
    pass

def Get_mv_name(headers,cookie):#用户输入电影/电视剧名称
    print("=====================================================================")
    print("                                                                   ")
    print("                                                                   ")
    print("                      电影爬虫                                      ")
    print("                                                                   ")
    print("                                                                   ")
    print("=====================================================================")
    print("输入的电影或者电视剧名称最好精确，否则网站可能查询不到。")
    mv_name=input("输入想看的电影或者电视剧名称：")
    return Search_mv_name(mv_name)
    # print(web.text.encode('gbk'))
    pass


def Search_mv_name(mv_name):#搜索电影/电视剧
    url = 'https://www.dy2018.com/e/search/index.php'
    mv_list=[]
    mv_more_list=[]
    mv_load=[]
    data = mv_name
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
    for i in (mv_load):
        i.replace('\\r','')
        print(str(i))

    # with open ("mv_load.txt","a+") as f:
    #
    #     for i in (mv_load):
    #
    #             i.replace('\\r','')
    #             f.write(i)
    # f.close()


    with open ("mv_more_list.txt",'a+') as f:
        f.write(str(mv_more_list))
        f.close()
    #     print('电影名称：',movie_name)
    #     print('详情页链接：',detail_link)
    #     print('下载链接：',download_link)
    # req = requests.post(url,data=data)
    # print(req.content)

    
    pass


def Get_mv_page():#获取电影/电视剧下载链接
    pass


def Download_mv():#下载视频
    pass


def Save_mv():#保存视频
    user_set = input("是否保存视频？（Y/N）\n")
    if user_set == 'Y':
        with open ("save_video.txt","a+") as f :
            f. write()
            f.close()
    elif user_set == 'N':
        exit()
    else :
        print("输入不正确请重新选择。（Y/N）")
    pass



def main():
    pass








if __name__ == '__main__':
    headers= headers()
    cookie = cookie()
    Get_mv_name(headers,cookie)
    pass
