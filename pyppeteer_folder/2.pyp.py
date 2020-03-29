"""

可以 爬取JavaScript渲染页面之后的内容

python.exe .\pyppeteer_folder\2.pyp.py
"""

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
 
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://quotes.toscrape.com/js/')
    doc = pq(await page.content())
    print('Quotes:', doc('.quote').length)
    await browser.close()
 
asyncio.get_event_loop().run_until_complete(main())