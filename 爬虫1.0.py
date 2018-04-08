# import requests
# from lxml import etree
#
#
# draw = 0
# #get 网页的函数
# def feach(url):
#     r = requests.get(url)
#     return r.text.replace('\t','')
#
# #解析每所大学地址
# def prase (html):
#     sele = etree.HTML(html)
#     links = sele.xpath('//*[@id="content"]/table/tbody/tr/td[2]/a/@href')
#     return links
#
# #解析爬虫每所大学的详细信息
# def prrase_new(link):
#     global draw
#     draw+=1
#     print(draw)
#     sele = etree.HTML(link)
#     tables = sele.xpath('//*[@id="wikiContent"]/div[1]/table/tbody')
#     #如果 tables为Flase则返回
#     if  not tables:
#         return
#     tables = tables[0]
#     keys = tables.xpath('./tr/td[1]//text()')
#     values = tables.xpath('./tr/td[2]')
#     #join 把文字中存在空格的链接起来
#     value = [''.join(value.xpath('.//text()')) for value in values]
#     info = dict(zip(keys, value))
#     print(info)
#
#
# if __name__ == '__main__':
#     url = 'http://qianmu.iguye.com/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D'
#     links = prase(feach(url))
#     for link in links:
#         if not link.startswith('http://'):
#             link = 'http://qianmu.iguye.com/%s' % link
#         prrase_new(feach(link))





import requests
from lxml import etree

from 爬虫补课.爬虫练习.craete_sql import down_db


def feach(url):
    r = requests.get(url)
    return r.text.replace('\t','')


def parse(html):
    etr = etree.HTML(html)
    links = etr.xpath('//*[@id="content"]/table/tbody/tr/td[2]/a/@href')
    return links

def parse_new(link):

        etr = etree.HTML(link)
        tables = etr.xpath('//*[@id="wikiContent"]/div[1]/table/tbody')

        if not tables:
            return
        tables = tables[0]
        key = tables.xpath('./tr/td[1]//text()')
        values = tables.xpath('./tr/td[2]')
        value = [''.join(value.xpath('.//text()')) for value in values]
        shcool = etr.xpath('//*[@id="wikiContent"]/h1/text()')[0]
        info = dict(zip(key, value))
        print(len(value))
        print(value)

        insert_table(shcool,value)


def insert_table(shcool,value):
    table = down_db()
    table.insert_tabale(shcool,value)


if __name__ == '__main__':
    url = 'http://qianmu.iguye.com/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D'
    links = parse(feach(url))
    for link in links:
        print(link)
        if not  link.startswith('http://') :
            link = 'http://qianmu.iguye.com/%s'%link
        parse_new(feach(link))















