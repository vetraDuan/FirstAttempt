#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :fs_login_test.py
# @Time      :2023/11/7 16:27
# @Author    :Vetra

import asyncio
import time
import sys
from pyppeteer import launch


async def run(loop, ascm_url, url_info, product, chrome_path, user_name, password):
    start_parm = {

        "executablePath": r"{}".format(chrome_path),
        "headless": True,

    }

    browser = await launch(**start_parm, options={'args': ['--no-sandbox']}, ignoreHTTPSErrors=True)

    page = await browser.newPage()

    await page.setUserAgent(
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36')

    await page.goto(ascm_url)

    xpath_username = await page.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[1]/div/span/input")
    xpath_password = await page.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[2]/div/span/input")
    but = await page.xpath("/html/body/div[1]/div/div[2]/div[2]/div/form/div[3]/div/button/span")

    await asyncio.sleep(0.1)
    await xpath_username[0].type(user_name)
    await asyncio.sleep(0.3)
    await xpath_password[0].type(password)
    await asyncio.sleep(0.4)
    await but[0].click()

    await page.waitForNavigation()
    await page.goto(url_info)
    # await page.waitForNavigation()

    page_text = ''
    try:
        page_text = await page.content()
    except:
        page_text = 'error'
    with open('/tmp/{}.txt'.format(product), 'w', encoding='utf-8') as file:

        import sys
        sys.stdout = file

        print(time.time())
        print(page_text)

        sys.stdout = sys.__stdout__
    await browser.close()
    loop.stop()


def main(ascm_url, url_info, product, chrome_path, user_name, password):
    loop = asyncio.get_event_loop()

    loop.run_until_complete(run(loop, ascm_url, url_info, product, chrome_path, user_name, password))

    loop.close()


if __name__ == '__main__':
    run_conf = sys.argv[1]
    run_conf = run_conf.split()
    ascm_url = run_conf[0]
    url_info = run_conf[1]
    product = run_conf[2]
    chrome_path = run_conf[3]
    user_name = run_conf[4]
    password = run_conf[5]
    main(ascm_url, url_info, product, chrome_path, user_name, password)
