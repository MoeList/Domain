#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import datetime
import time

qq='接收信息的QQ'
port='12513'
domain='要监控的域名'

if __name__ == '__main__':
    while (1==1):
        requests.get('http://127.0.0.1:' + port + '/send_private_msg?user_id=' + qq + '&message=域名检测启动成功')
        res = requests.get('https://api.moeclub.org/whois/' + domain)
        res = res.text.split("\n")
        #print(res)
        for a in res:  # 第一个实例
            b = a
            if 'Registry Expiry Date:' in a:
                break
        res = b[22:-1].split('T')
        d1 = datetime.datetime.strptime(res[0], '%Y-%m-%d')
        d2 = datetime.datetime.now()
        res = (d1 - d2)
        if res.days < 90:
            requests.get('http://127.0.0.1:'+port+'/send_private_msg?user_id='+qq+'&message=域名到期警告！还有'+str(res.days)+'天域名到期！')
        time.sleep(86400)