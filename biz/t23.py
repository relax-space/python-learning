import json

import xmltodict

t1 = '''
<servers>
  <server>
    <name>host1</name>
    <os>Linux</os>
    <interfaces>
      <interface>
        <name>em0</name>
        <ip_address>10.0.0.1</ip_address>
      </interface>
    </interfaces>
  </server>
</servers>
'''
content = xmltodict.parse(t1, force_list=['servers', 'interfaces'])
data_str = json.dumps(content)
print(data_str)
