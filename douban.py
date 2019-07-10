#!/usr/bin/env python
# -*- coding:utf-8 -*-
#coder:郑宇星
#date:18/7/25

import requests
requests = requests.Session()

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
    'Referer':'https://www.douban.com/'
}

def login():
    response = requests.get('https://www.douban.com/j/misc/captcha',headers=headers)
    result = response.json()
    captchaurl = result['url']
    captchatoken = result['token']
    response = requests.get('https:'+captchaurl,headers=headers)
    codeImg = response.content
    fn = open('cap.png','wb')
    fn.write(codeImg)
    fn.close()
    data = {
        'source':'index_nav',
        'form_email':'792726304@qq.com',
        'form_password':'zyx792726304',
        'captcha-solution':input("请输入验证码："),
        'captcha-id':captchatoken
    }
    response = requests.post('https://www.douban.com/accounts/login',headers=headers,data=data)
    if '郑' in response.text:
        print("登陆成功")
    else:
        login()
def other():
    response = requests.get('https://www.douban.com/people/181735310/',headers=headers)
    print(response.text)
login()
other()