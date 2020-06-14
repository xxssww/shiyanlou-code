#!/home/shiyanlou/anaconda3/bin/python

import requests
from lxml import html
import re

def user_info(user_id):
    content = requests.get('https://www.shiyanlou.com/users/%s' % user_id)

    tree = html.fromstring(content.text)
    if content.status_code  == 200:
        user_name1 = tree.xpath('//div[@class="user-meta"]/span[1]/text()')
        user_level1 = tree.xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[1]/span[2]/text()')
        join_date1 = tree.xpath('//*[@id="__layout"]/div/div[1]/div[1]/div[1]/div/div[1]/div[2]/span/text()')
        user_name = ''.join(user_name1[0].split())
        user_level = ''.join(re.findall(r'\d+',user_level1[0]))
        user_level = int(user_level)
        join_dates = join_date1[0].split()
        join_date = ''.join(join_dates[0].split())
        print(user_name,user_level,join_date)
        return user_name,user_level,join_date
    else:
        user_name,user_level,join_date = (None,None,None)
        return user_name,user_level,join_date

user_info("214893")
user_info("1234567890")



