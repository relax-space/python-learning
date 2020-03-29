"""
python.exe .\pyppeteer_folder\4.login_tmall.py
"""

import asyncio
from pyppeteer import launch
 
async def main():

    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await asyncio.sleep(100)
 
asyncio.get_event_loop().run_until_complete(main())