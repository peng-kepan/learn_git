import  datetime
import re #正则表达式模块
p=r'\w+@zhijieketang\.com'#正则表达式
email1='panpan@zhijieketang.com'
#m=re.match(p,email1)#匹配
#m=re.search(p,email1)
m=re.findall(p,email1)
#c=re.sub(r'\d+',' ','AB12i9F7j8')#替换字符串
c=re.split(r'\d+','AB12i9F7j8',maxsplit=1)#分割字符串
print(c)

print(m)

# d=datetime.datetime(2022,8,9,18,54,22)
#
# print(d.today(),d.now(),d.fromtimestamp(999999999),d.date(),d.time())
#
# dd=datetime.date.today()
# delta=datetime.timedelta(10)#datetime.timedelta表示两个时间的间隔
# dd+=delta
# print(dd.strftime('%Y-%m-%d %H:%M:%S'))

