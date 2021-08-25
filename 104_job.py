import time
import os
import json
import requests
from bs4 import BeautifulSoup
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
headers = {
    'User-Agent':userAgent
}
url = 'https://www.104.com.tw/jobs/search/?keyword=資料分析師&page=%s'
for i in range(0,10):
    res = requests.get(url%(i), headers = headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    jobs = soup.select('div[class="b-block__left"]')
    for job in jobs:
        try:
            pre_new_url = job.select('a[class="js-job-link"]')[0]
            aa = str(pre_new_url["href"]).split('b/')[1].split('?')[0]
            new_url = f'https://www.104.com.tw/job/ajax/content/'+aa
            new_headers = {
                'User-Agent':userAgent,
                'Referer': f'https://www.104.com.tw/job/'+aa
            }
            new_res = requests.get(new_url, headers = new_headers)
            job_content = new_res.json()
            print("===========================職缺============================")
            print(job_content['data']['header']['jobName'])
            print(job_content['data']['header']['custName'])
            print("-------------------------工作項目---------------------------")
            print(job_content['data']['jobDetail']['jobDescription'])
            print('網址： https://www.104.com.tw/job/'+aa+'\n')
        except :
            print("")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~next page')





