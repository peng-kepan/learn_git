# var = 'asdfghj'
# print(var[0])#print(var[索引])
# print(var[1:5])
# print(var[1:5:3])

# str_a='qwe\nrtyu'
# str_b='''好好学习
# 天天向上'''
# print(str_a)
# print(str_b)

# a =['a','p','p','l','e']
# print(" 、".join(a))

# b='apple'
# print(b.split('p'))

# food='orange'
# if food=='apple':
#     print('apple')
# elif food=='banana':
#     print('banana')
# elif food=='orange':
#     print('orange')
# else:
#     print('other')

# a=[1,2,3,4,5]
# for i in a:
#     print(i)

# for i in range(1,101):
#     print(i)

# sum=0
# for i in range(0,101,2):
#       sum+=i
# print(sum)

# import random
# # for i in range(100):
# i = random.randint(1, 100)
# print('-----{}-----'.format(i))
# while True:
#     p=int(input("请输入你猜的数字： "))
#     print(p)
#     if p>i:
#         print("小一点")
#     elif p<i:
#         print('大一点')
#     elif p==i:
#         print('猜对了')
#         break
# sum=0
# # for i in range(1,101):
# #     if i%2==1:
# #       sum+=i
# for i in range(1,100,2):
#     sum+=i
#     print(i)
# sum=0
# x=1
# while x<=100:
#     if x%2==1:
#         sum+=x
#     x+=1
# print(sum)


# li=list()
# print(type(li),li)
# li1=list('hello')
# print(type(li1),li1)
# li2=[i for i in range(1,10) if i%2==0]
# print(type(li2),li2)
# li3=[1]
# li3.append('panpan')#末尾新增
# li3.extend('pkkp')#末尾新增每个字符
# li3.insert(2,'abc')#指定位置
# li3.pop()
# li3.remove('p')
# print(len(li3),li3)
# print(li2+li3)

# li=[1,3,2,34,2,7]
# li.sort(reverse=True)#从大到小
# li.sort()   # #从小到大
# li.reverse()#倒排
# print(li)

# result=[]
#
# for i in range(1,11):
#     if i%2==0:
#         result.append(i**2)
# print(result)
#
# result=[i **2 for i in range(1,11) if i%2==0]  #推导式
# print(result)

#元组() 列表[]  集合{}
# t1=(1,2,3,4,5,1)
# print(type(t1),t1,t1[2],t1[-1],t1[::2],t1.index(3),t1.count(1))  #index  返回索引值 #count 返回元组中出现的总次数

# set1={1,2,3}
# print(type(set1))
#
# set2=set('hello')
# print(set2,type(set2))
#
# set3=set([1,2,3])
# print(set3,type(set3))

# #推导式
# set4={i for i in range(0,5) if i%2==0 }
# print(set4)

# set5={1,4,6,7}
# print(1 in set5,1 not in set5)
# set5.add('heloow')
# print(set5)
# set5.update('qyi','po')
# print(set5)
# set5.remove(1)  #remove移除不存在的将会报错
# print(set5)
# set5.discard(4)
# print(set5)
# set5.discard(100) #discard移除不存在的不会报错
# print(set5)
# set5.pop()  #pop随机删除
# print(set5)


# a={1,2,3}
# b={2,3,4}
# #交集
# print(a&b)
# print(a.intersection(b))
# #并集
# print(a|b)
# print(a.union(b))
# #差集
# print(a-b)
# print(a.difference(b))

# set1 = set()
# for i in 'hogwartsss':
#     if i in 'hello world':
#         set1.add(i)
# print(set1)
#
# set1 = {i for i in 'hogwartsss' if i in 'hello world'}
# print(set1)

# dc1={'name':'pp','age':'28'}
# dc1['age']=18
# dc1['sex']='girl'
# print(dc1,type(dc1),dc1['age'],dc1['name'],dc1.items(),dc1.keys(),dc1.values(),dc1.get('age'))
#
# data={'age':111}
# dc1.update(data)
# print(dc1)
# dc1.pop('age')
# print(dc1)


# dic={ k:v for k,v in[{'name','age'},{'pp',18}]}
# print(dic)

# dic={'a':1,'b':2,'c':3}
# new={v:k for k,v in dic.items()}
# print(new)













