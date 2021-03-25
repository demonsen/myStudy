
#!/usr/bin/env python3
# coding:utf-8

import requests
import time
import sys
import os
import inspect

url="http://kaoqin.adsage.com/iclock/accounts/login/"

def URL_respon(code = 200, retries = 3):
    try: 
        html = requests.get(url,timeout=0.1)
        print("【%s】 返回码 %s" % ( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), html.status_code))
    except Exception as e:
        print(e)
        if retries > 0:
            return URL_respon(code, retries-1)
        else:
            return False
    
    if html.status_code == code:
        return True
    else:
        return URL_respon(code, retries-1)

if __name__=='__main__':
    
    if URL_respon(200, 3):
        print("【 %s 】 访问正常.." % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    else:
        print("【 %s 】 访问异常.." % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))




