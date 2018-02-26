#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/15 15:29
# @Author  : milian0711
# @File    : upload_picture.py

import requests

base = 'http://60.174.236.109:8090'

loginUrl = base + '/www/user-login-L3d3dy9teS5odG1s.html'

h = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Referer': 'http://60.174.236.109:8090/www/user-login-L3d3dy9teS5odG1s.html',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Connection': 'keep-alive'
}

body = {
    'account': 'hh',
    'password': '11',
    'referer': '/www/my.html',
    'keepLogin[]':'on'
}

s = requests.session()
r = s.post(loginUrl, data=body, headers=h)
print r.content

url1 = base + '/www/bug-create-1-0-moduleID=0.html'

data = {
    # 'localUrl':(None, 'E:\\wm.png'),
    # "imgFile": ("wm.png", open("E:\\wm.png", "rb"), "image/png")
    "product": "1",
    "module": "0",
    "project": "",
    "openedBuild[]": "trunk",
    "assignedTo": "huanglijuan",
    "type": "codeerror",
    # "os": "all",
    # "browser": "all",
    # "color": "",
    "title": "提交1",
    "severity": "3",
    "pri": "0",
    "steps": '<p>[步骤]</p>\
                <p>1、第一步点</p>\
                <p>2、第二步点</p>\
                <p>3、点三步点</p>\
                <p>[结果]</p>\
                <p>我是结果</p>\
                <p>[期望]</p>',
    # "story": "0",
    "task": "0",
    # "mailto[]": "",
    # "keywords": "",
    # "files[]": ("1.png", open("d:\\1.png", "rb"), "image/png"),
    # "labels[]": "tu1",
    # "uid": "5a2955c884f98",
    "case": "0",
    "caseVersion": "0",
    "result": "0",
    "testtask": "0"
}

file = [
("files[]", ("wm.png", open("E:\\wm.png", "rb"), "image/png")),
("labels[]", "tu3"),
("files[]", ("wm.png", open("E:\\wm.png", "rb"), "image/png")),
("labels[]", "tu4"),
]

r = s.post(url1, data=data, files=file)
print r.content