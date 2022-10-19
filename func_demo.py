# def func_demo():
#     print('hello  world')
#
# def func_with_params(a,b,c):
#     '''
#     :param a: aaaa
#     :param b: bbbb
#     :param c: cccc
#     :return:
#     '''
#     print('a={a},b={b},c={c}')
#
#
# func_demo()
# func_with_params(1,2,3)

#可变参数元组
# def print_language(*args):
#     print(args)
#     for i in args:
#         print(i)
#
# print_language('python','java','php','go')
#
# #可变参数字典
# def print_info(**kwargs):
#     print(kwargs)
#
#
# print_info(name='pp',age=28)
#
# data={
#     'name':'pp',
#     'age':18
# }
# print_info(**data)
import sys

import gender as gender


# class Person:
#     def __init__(self,name,age,gender,weight):
#        self.name = name
#        self.age = age
#        self.gender = gender
#        self.weight = weight
#     @classmethod
#     def eat(cls):
#         print('eating')
#
#     def play(self):
#         print('playing')
#
#     def jump(self):
#         print('jump')
#
# class Girl(Person):
#     @classmethod
#     def eat(self):
#         print('chichichi')
#
#
# pp=Person('pp',18,'girl',97)
# print(pp.name,pp.age,pp.weight,pp.gender)
# Person.eat()
# Girl.eat()
#
#
# class StaticMethod:
#     @staticmethod
#     def static_dome():
#         print('这是一个静态方法')
#
#
# StaticMethod.static_dome()


# class DateFormat:
#     def __init__(self,year=0,month=0,day=0):
#         self.year = year
#         self.month = month
#         self.day = day
#     def out_date(self):
#         return f'{self.year,self.month,self.day}'
#     @classmethod
#     def json_format(cls,json_data):
#         year, month, day = json_data['year'],json_data['month'],json_data['day']
#         return cls(year, month, day)
#
# json_data={'year':2022,'month':9,'day':26}
# demo= DateFormat.json_format(json_data)
#
# print(demo.out_date())
#
# def  search():
#     print("zheshiyige fangfa")


# li = {'pp','oo','ii'}
# ll = {'name':'pp','age':18}
#
# print('shide:{},{},{}'.format(*li))
# print("shi:{name},{age}".format(**ll))   #字典解包** ，传入key
#
# print(f"my name is {ll['name']} ,age is ")


with open('/Users/Fan/PycharmProjects/pythonProject3/venv/data.txt','r') as f:
    # for i in f.readlines():
    #   print(i)
    while True:
        line=f.readline()
        if line:
            print(line)
        else:
            break
      





