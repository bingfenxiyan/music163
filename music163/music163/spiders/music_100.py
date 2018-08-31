# -*- coding: utf-8 -*-
import time
import random
import scrapy
import re
import json
import datetime


from music163.items import Music163Item
from music163.settings import MAX_COUNT


class Music100Spider(scrapy.Spider):
    name = 'music_100'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/discover/toplist?id=3778678']
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_574566207'

    def parse(self, response):
        count = 0
        html = response.text
        html = re.findall('<ul class="f-hide">(.*)</ul>',html)
        froms = re.findall('<li><a href="\/song\?id=(\d*)">([\s\S]*?)</a></li>', html[0])
        for mId,name in froms:
            if name == '可能否':
                return
            url_id = self.url + str(mId)+'?limit=20&offset=0'
            request = scrapy.Request(url_id, dont_filter=True, callback=self.parse_music)
            request.meta['count'] = count       #传递参数给下一个爬虫
            request.meta['name'] = name
            yield request

    def parse_music(self,response):
        '''爬取每首歌的评论,从meta中获取url的初始化count参数'''
        count = response.meta['count']
        musicName = response.meta['name']
        need_uri = str(response.url)
        need_u = re.findall('(http:\/\/music\.163\.com\/api\/v1\/resource\/comments\/R_SO_4_\d*\?limit=20&offset=)', need_uri)[0]
        uri = need_u + str(count)
        print('--------->',uri)
        # 解析获取的json数据，得到评论和用户信息
        htmls = json.loads(response.text)['hotComments']
        # {   json全部的数据格式为下，获取有用的信息:用户id,用户昵称,点赞数,时间,评论
        # "user":
        #   {"locationInfo":null,
        #    "authStatus":1,
        #    "remarkName":null,
        #    "avatarUrl":"http://p1.music.126.net/amEMEIvy6mXcezs22MNKzA==/109951163385713971.jpg",
        #    "experts":null,
        #    "userId":307312386,    用户id
        #    "vipType":11,
        #    "nickname":"李佳隆JelloRio",    用户昵称
        #    "vipRights":{
        #           "associator":{"vipCode":100,"rights":true},
        #           "musicPackage":{"vipCode":200,"rights":true}},
        #    "userType":4,
        #    "expertTags":null},
        # "beReplied":[],               回复的是谁的评论的信息
        # "pendantData":null,
        # "liked":false,
        # "likedCount":249089,          点赞数目
        # "commentId":1195883948,
        # "time":1532779444512,         时间戳为  -->1532779444 + 8小时
        # "expressionUrl":null,
        # "content":"对不起大家[流泪]，太紧张没听清楚还错拍了。"     评论
        # },
        for html in htmls:
            item = Music163Item()
            item['userId'] = html['user']['userId']
            item['nickname'] = html['user']['nickname']
            item['likedCount'] = html['likedCount']
            item['time'] = html['time']
            item['content'] = html['content']
            item['musicName'] =musicName
            yield item

        # 给出获取的最深评论页数MAX_COUNT，防止系统死机
        if count == MAX_COUNT:
            return
        else:
            count += 20
            request = scrapy.Request(uri, dont_filter=True, callback=self.parse_music)
            request.meta['count'] = count
            request.meta['name'] = musicName
            time.sleep(random.randint(2,5))     #随机睡眠2-5s，防止反爬
            yield request


