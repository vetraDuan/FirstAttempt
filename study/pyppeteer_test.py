# -*- coding:utf-8 -*-
# author: vetra

import asyncio
from pyppeteer import launch

# executablePath = '/root/.local/share/pyppeteer/local-chromium/588429/chrome-linux'
executablePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'


async def main():
    browser = await launch(executablePath=executablePath, options={'args': ['--no-sandbox']})
    page = await browser.newPage()
    await page.goto('https://www.baidu.com/')
    content = await page.content()
    print(content)

    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
