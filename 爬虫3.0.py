
import requests
import threading
import redis
from queue import Queue
from lxml import etree


r = redis.Redis()
link_queue = Queue()
DOWNLOADNUM = 50


def feach(url,raise_err =False):
    r = requests.get(url)
    try:
        r = requests.get(url)
    except Exception as e:
        print(e)
    else:
        if raise_err:
            r.raise_for_status()  # 返回的状态码不是200报错
    return r.text.replace('\t','')


def parse(html):
    etr = etree.HTML(html)
    links = etr.xpath('//*[@id="content"]/table/tbody/tr/td[2]/a/@href')
    for link in links:
        if not  link.startswith('http://') :
            link = 'http://qianmu.iguye.com/%s'%link

        # link_queue.put(link)
        if r.sadd('qianmu11.seen',link):

             r.lpush('qianmu11.queue',link)

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
        print(info)
        r.lpush('qianmu11.item',info)

def download():
    while True:
        link = r.rpop('qianmu11.queue')
        # link = link_queue.get()
        if link == None:
            break
        parse_new(feach(link))
        link_queue.task_done()
        print(link)

        print('任务：%s'%link_queue.qsize())


if __name__ == '__main__':
    url = 'http://qianmu.iguye.com/2018USNEWS%E4%B8%96%E7%95%8C%E5%A4%A7%E5%AD%A6%E6%8E%92%E5%90%8D'
    parse(feach(url,raise_err =True))
    for i in range(DOWNLOADNUM):
        t = threading.Thread(target=download)
        t.start()
    link_queue.join()
    for i in range(DOWNLOADNUM):
        link_queue.put(None)

