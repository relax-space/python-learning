"""
python.exe .\pyppeteer_folder\5.cookie_tmall.py
"""

import asyncio
import random
import time

from pyppeteer import launch


async def page_evaluate(page):
    # 替换淘宝在检测浏览时采集的一些参数
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }''')
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')


async def taobao_login(username, password):
    # 'headless': False如果想要浏览器隐藏更改False为True
    browser = await launch({
        'headless': False,
        'executablePath': r'C:\Users\Administrator\AppData\Local\pyppeteer\pyppeteer\local-chromium\880765\chrome-win\chrome.exe',
        'userDataDir': r'D:\2.file\chromium\userData',
        'args': ['–no-sandbox'],
        'dumpio': True})
    # context = await browser.createIncogniteBrowserContext() #  开启无痕浏览器模式
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    await page.goto("http://g.burgeon.cn:988/c/portal/login")
    # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果
    await page_evaluate(page)
    # try:
    #     await page.click('img[id="chkimg"]')  # 直接点击手机登录
    # except:
    #     pass
    # 选中输入框
    # print(await page.content())  # 获取所有html内容
    element = await page.J('#login')
    input_text = await (await element.getProperty('value')).jsonValue()  # 获取内容
    if input_text:
        # 删除输入框里的内容
        await element.click({'clickCount': 3})  # 单击输入框三次选中
    # 清空输入框里的内容
    await page.waitFor(1000)
    # 输入用户名，密码
    # delay是限制输入的时间
    await page.type('#login', username, {'delay': input_time_random() - 50})
    await page.type('#password1', password, {'delay': input_time_random()})
    # await page.click('#J_SubmitStatic')
    await page.waitFor(10000)
    # cookies2 = await page.cookies()
    # cookie = "; ".join(["%s=%s" % (i['name'], i['value']) for i in cookies2])
    # print(f'cookie{cookie}')
    # await page.close()
    # # await context.close()
    # await browser.close()
    # return cookie


def input_time_random():
    return random.randint(100, 151)


if __name__ == '__main__':
    username = 'xiao.xinmiao@burgeon.cn'
    password = '123'
    # files = open("./cookies.txt", "a")
    task = asyncio.get_event_loop().run_until_complete(
        taobao_login(username, password))
    print(task)
    # files.write(task+"\n")
