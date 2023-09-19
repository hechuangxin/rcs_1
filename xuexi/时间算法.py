from datetime import datetime, timedelta

date1 = datetime(2023, 4, 23, 10, 8, 41)
date2 = datetime(2023, 4, 12, 18, 15, 3)

diff = date1 - date2

# 计算总秒数并保留两位小数
seconds = round(diff.total_seconds(), 2)
print(seconds)

# 计算总分钟数并保留两位小数
minutes = round((diff.total_seconds() / 60), 2)
print(minutes)
