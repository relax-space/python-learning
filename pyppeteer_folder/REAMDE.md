目标：使用pyppeteer模拟浏览器操作

说明：
Pyppeteer 是依赖于 Chromium 这个浏览器来运行的
Chromium（开源，开发版本） ==>  Chrome（正式版）

获取cookie的步骤：
1.获取chromium版本 以及下载地址：python.exe .\pyppeteer_folder\0.version.py
2.下载chromium：
3.本地创建文件夹：并将chrome放在对应的地方
4.获取cookie：记得先给username 和 password赋值，`python.exe .\pyppeteer_folder\5.cookie_tmall.py`

```
'executablePath':r'D:\file\chromium\chrome-win32\chrome.exe',
'userDataDir': r'D:\file\chromium\userData',
```

参照：
https://cuiqingcai.com/6942.html