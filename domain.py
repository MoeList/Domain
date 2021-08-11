#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import datetime
import time

qq='接收信息QQ'
port='5700'

if __name__ == '__main__':
    while (1==1):
        with open('domainlist.txt', "r") as f:
            for line in f.readlines():
                domain = line.strip('\n')
                res = requests.get('https://api.moekee.com/whois/'+ str(domain))
                res = res.text.split('\n')
                for a in res:
                    b = a
                    if 'Registry Expiry Date:' in a:
                        break
                res = b[22:-1].split('T')
                d1 = datetime.datetime.strptime(res[0], '%Y-%m-%d')
                d2 = datetime.datetime.now()
                res = (d1 - d2)
                if res.days < 0:  #想要的时间
                    requests.get('http://127.0.0.1:' + port + '/send_private_msg?user_id=' + qq + '&message=域名删除提醒！！！\n''域名：' + str(domain) + '\n已到期 ' + str(res.days) + ' 天！')
                    time.sleep(5)  # 多个域名检测中间间隔秒数（没试过 0 秒）
                elif res.days <= 60:
                    requests.get('http://127.0.0.1:' + port + '/send_private_msg?user_id=' + qq + '&message=域名到期提醒！！！\n''域名：' + str(domain) + '\n还有 ' + str(res.days) + ' 天域名到期！')
                    time.sleep(5)  # 多个域名检测中间间隔秒数（没试过 0 秒）
                elif res.days > 60:
                    time.sleep(5)  # 多个域名检测中间间隔秒数（没试过 0 秒）
        time.sleep(86400)   #多少秒跑一次
