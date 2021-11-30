
import datetime
from typing import Dict, List

from chinese_calendar import is_holiday


def get_dates(start: datetime, end: datetime) -> List[str]:
    date_8_list: List[str] = []
    while start <= end:
        if is_holiday(start):
            start += datetime.timedelta(days=1)
            continue
        date_8_list.append(start.strftime('%Y%m%d'))
        start += datetime.timedelta(days=1)
    return date_8_list


end = datetime.datetime.today()
start = end + datetime.timedelta(-6)

start = datetime.datetime(2021, 2, 1)
print(get_dates(start, end))
