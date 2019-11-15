'''
2019/11/15
多线程爬取小说、保存
ko
'''

import re
import requests
import time
import os
from multiprocessing.dummy import Pool

#保存小说的目录
os.makedirs('book' , exist_ok=True)

url = 'http://m.yuetutu.com/mbook_4883/{}.html'
url_li = [url.format(i) for i in range(1,1000)]
pool = Pool(10)

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    html = requests.get(url , headers = headers)
    # print(html.text)
    time.sleep(5)  #防止被恶意消耗服务器资源
    get_data(html.text)
    # return html.text

def get_data(page):
    title = re.search(r'<title>《(.*?)》-绝世药神-笔趣阁</title>' ,page).group(1)
    txt = re.findall(r'</p>(.*?)<p>' , page , re.S)[1].replace('&nbsp' , '').replace('<br/>' , '\n').replace(';' ,'' )

    with open('./book/{}.txt'.format(title) , 'w') as f:
        f.write(txt)
        print('save {} is ok'.format(title))




if __name__ == "__main__":

    pool.map(get_page,url_li)
    # pool.map( get_page, (pool.map(get_data , url_li)))


