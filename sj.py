# coding=utf-8
import random
import string
#ht=random.randint(1,50)
#ht=random.randrange(10)
#ht='HJ'.join(random.sample(string.ascii_letters + string.digits, 8))
# ht='HJ'
# for i in range(6):
#     aa=str(random.randint(0,9))
#     ht+=aa
#
# print(ht)

#score = int(input("请输入一个0～100的整数"))
# if score >= 60:
#     if score >= 85:
#         print('你真优秀')
#     else:
#         print('你真好')
# else:
#     print('你需要努力')

# if score >= 90:
#     grade ='A'
# elif score >= 80:
#     grade ='B'
# elif score >=70:
#     grade ='C'
# elif score>=60:
#     grade = 'D'
# else:
#     grade = 'E'
# print('Grade = '+grade)

# for i in 'Hello':
#     print(i)
#
# for i in [1,3,2,4,56,8]:
#     print(i)
#

# i=0
#
# while i*i <1000:
#     i+=1
#
# print('i=',i)
# print('i*i=', i*i)

# for i in range(10):
#     if i ==3:
#         #break
#         continue
#     print(i)

#print('Hello\nworld{0}'.format(1))


# s='Hello world'
# print(s.find('l'))#查找
# print(s.find('l',6,8))
# print(s.find('l',8))
# print(s.replace('l','p',1))#替换
# print(s.split('l'))#分割

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def calc(opr):
    if opr =='+':
        return add
    else:
        return sub

#匿名函数
def calc2(opr):
    if opr =='+':
        return  lambda a,b:(a+b)
    else:
        return  lambda a,b:(a-b)

def pp(name='panpan'):
    return name
#元祖可变参数
def sum(*numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total
#字典可变参数
def show_info(**info):
    print('==========')
    for key,value in info.items():
        print('{0}-{1}'.format(key,value))


def gl(x):
    return x > 50

def f1(x):
    return x * 2

if __name__ == '__main__':
    # d=add(12,24)
    # print(d)
    # p=pp()
    # a=pp('luoluo')
    # print(p,a)
    # a=sum(20,100,300)
    # print(a)
    # show_info(s_id=123,s_name='panpan')

    i=calc2('+')
    print(i(10,5))

    # data=[66,12,90,0,9,67]
    # filtered=filter(gl,data)#过滤函数
    # data2=list(filtered)
    # print(data2)
    # mapped=map(f1,data)#映射函数
    # data3=list(mapped)
    # print(data3)


