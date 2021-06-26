import time
import datetime
# strftime 指令 含义
# %Y                    带世纪的年份，例如'2014'
# %y                    不带世纪的年份，'00'至'99'（1970 至 2069）
# %m                    数字表示的月份, '01'至'12'
# %B                    完整的月份，例如'November'
# %b                    简写的月份，例如'Nov'
# %d                    一月中的第几天，'01'至'31'
# %j                    一年中的第几天，'001'至'366'
# %w                    一周中的第几天，'0'（周日）至'6'（周六）
# %A                    完整的周几，例如'Monday'
# %a                    简写的周几，例如'Mon'
# %H                    小时（24 小时时钟），'00'至'23'
# %I                    小时（12 小时时钟），'01'至'12'
# %M                    分，'00'至'59'
# %S                    秒，'00'至'59'
# %p                    'AM'或'PM'
# %%                    就是'%'字符
oct21st = datetime.datetime(2021, 6, 26, 13, 56, 0)
print('年月日 时分秒: ', oct21st.strftime("%Y-%m-%d %H:%M:%S"))
print('12小时制时分秒: ', oct21st.strftime("%I:%M:%S %p"))
print('完成的月份和不带世纪的年: ', oct21st.strftime("%B of '%y"))
print('今天是一年中的第 ', oct21st.strftime('%j'), ' 天')
print('今年还剩下 ', 365 - int(oct21st.strftime('%j')), ' 天')
print('今天是一周中的第 ', oct21st.strftime('%w'), ' 天')
octDateTime = datetime.datetime.fromtimestamp(time.time())
print('今天是: ', octDateTime)
startTime = time.time()
print('startTime: ', startTime)
print(datetime.datetime.strptime('June 26, 2021', '%B %d, %Y'))
print(datetime.datetime.strptime('2021/06/26 14:59:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime("June of '21", "%B of '%y"))
print(datetime.datetime.strptime("June of '63", "%B of '%y"))
