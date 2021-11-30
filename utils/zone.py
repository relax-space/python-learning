from datetime import datetime,timedelta,timezone
TZ_BJ = timezone(timedelta(hours=8))

print(datetime.now(TZ_BJ))
print(datetime(2021,12,20,17,tzinfo=TZ_BJ))