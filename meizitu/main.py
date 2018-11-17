#!/usr/bin/env python3
#coding:utf-8
# Project Name: spider
# Create Time: 17:15
# User: zuona

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","meizitu"])

