# -*- coding:utf-8 -*-
"""
---------------------------------------
@Auth    :liugang
@Time    :2023/10/18 10:15
@Email   :1512499027@qq.cn
@IDE     :PyCharm
@Project :adbos-beijing 
@File    :robot.py
---------------------------------------
"""
import requests

import schedule


def robot1():
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=54a0205c-5fca-4b54-b3f5-f09a16b329f7"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "msgtype": "news",
        "news": {
            "articles": [
                {
                    "title": "家人们，补一下日报吧！！！",
                    "mentioned_mobile_list": ["@all"],
                    "description": "北京银行SDL项目进度看板",
                    "url": "https://doc.weixin.qq.com/sheet/e3_AFwApwarAAgdUFwCMNOQjy1054Ht7scode=ABIA8Ac5AA8d1VCbrSAdwAzAbpAPw&version=4.1.10.6011&platform=win&tab=o0dv3t",
                    "picurl": "http://www.blingsec.cn/uploads/images/20211126/c9340d45d9dbcab1bbc98668ce83861f.jpg"
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=data)
    records = response.json()
    return records


robot1()

def robot2():
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=0017cbc5-306e-4566-8ea2-ae005775a2da"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "msgtype": "news",
        "news": {
            "articles": [
                {
                    "title": "各位大佬们，求求你们了，补充下文档吧",
                    "mentioned_mobile_list": ["@all"],
                    "description": "民生银行开发同步文档",
                    "url": "https://h38ozbw2bw.feishu.cn/docx/KQTpd25iOov6pcxNNQEcGTj8npb",
                    "picurl": "http://www.blingsec.cn/uploads/images/20211126/c9340d45d9dbcab1bbc98668ce83861f.jpg"
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=data)
    records = response.json()
    return records


robot2()
# schedule.every().day.at('16:48').do(robot1, robot2)
# while True:
# schedule.run_pending()
