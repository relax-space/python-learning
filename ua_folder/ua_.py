r"""
获取随机的ua
python.exe .\ua_folder\ua_.py
"""

import shadow_useragent

ua = shadow_useragent.ShadowUserAgent()
for i in range(0,10):
    user_agent = ua.random
    print(user_agent)