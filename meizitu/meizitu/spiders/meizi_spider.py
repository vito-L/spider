#!/usr/bin/env python
# coding:utf-8
# Project Name: meizitu
# Create Time: 12:46
# User: zuona

import scrapy
import configparser
import re
import json
import datetime
# from meizitu.items import MeizituItem

from scrapy.exceptions import *
from scrapy.crawler import CrawlerProcess


class meizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['pixiv.net']
    start_urls = ['http://www.pixiv.net']
    headers = {
        "Origin": "https://accounts.pixiv.net",
        "Regerer": "https://accounts.pixiv.net/login?lang=zh",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
    }

    def parse(self, response):
        pass

    """登录并保存和跟踪COOKIE"""

    def start_requests(self):
        return [scrapy.Request(url='https://accounts.pixiv.net/login', callback=self.login)]

    def login(self, response):
        # 读取ini载入用户名和密码
        config = configparser.ConfigParser()
        config.read('login.ini')
        username = config.get('info', 'username')
        password = config.get('info', 'password')
        post_key = response.css('#old-login input[name=post_key]::attr(value)').extract_first()
        post_url = "https://accounts.pixiv.net/login?lang=zh"
        post_data = {
            "post_key": post_key,
            "pixiv_id": username,
            "password": password
        }

        return [scrapy.FormRequest(
            url=post_url,
            formdata=post_data,
            headers=self.headers,
            callback=self.check_login
        )]

    def check_login(self, response):
        # 验证登录是否成功
        if response.url == "https://www.pixiv.net/":
            print("login success")
        else:
            print("login false")
        pass
