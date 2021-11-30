import re


def regex_en(raw: str) -> bool:
    if (not raw) or (len(raw) != 4):
        return False
    result = re.findall(r'[A-Z]+', raw)
    value = ''.join(result)
    if len(value) != 4:
        return False
    return True


print(regex_en('wqWsWsDF'))
