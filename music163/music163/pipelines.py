# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import pymongo
from music163.settings import MONGO_URL, MONGO_PORT, MONGO_DB


class Music163Pipeline(object):
    def __init__(self):
        '''创建连接数据库所需要的变量'''
        self.url = MONGO_URL
        self.port = MONGO_PORT
        self.database = MONGO_DB

    def prices_item(self,item):
        '''对给过来的时间戳进行转换成具体时间'''
        item['time'] = datetime.datetime.utcfromtimestamp(int(str(item['time'])[:10])+28800).strftime("%Y-%m-%d %H:%M:%S")
        return item

    def process_item(self, item, spider):
        # if isinstance(item, Music163Item):
        #     client = pymongo.MongoClient(host=self.url, port=self.port)
        #     mydb = client[self.database]
        #     collection = item['musicName']      #根据不同的歌曲创建不同的集合
        #     post = mydb[collection]
        #     item = self.prices_item(item)
        #     data = dict(item)
        #     post.insert(data)           #将数据保存到对应的集合中去
        #     print('---->OK')
        #     client.close()              #关闭数据库连接  *很重要*
        #     return item
        item = self.prices_item(item)
        item = dict(item)
        with open('music200.csv', 'a') as f:
            f.write(str(item['userId']))
            f.write(',')
            f.write(item['nickname'])
            f.write(',')
            f.write(str(item['likedCount']))
            f.write(',')
            f.write(item['time'])
            f.write(',')
            f.write(item['content'])
            f.write(',')
            f.write(item['musicName'])
            f.write('\n')

