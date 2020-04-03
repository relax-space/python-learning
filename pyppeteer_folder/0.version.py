"""

chromium version

默认版本是：575458
# 可执行文件默认路径：C:\Users\Administrator\AppData\Local\pyppeteer\pyppeteer\local-chromium\575458\chrome-win32\chrome.exe
win64平台下载链接为：https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/575458/chrome-win32.zip

python.exe .\pyppeteer_folder\0.version.py

"""
import pyppeteer.chromium_downloader
print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('win64')))
print('win64平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('win64')))