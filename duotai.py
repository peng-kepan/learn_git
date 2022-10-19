def start(obj):
    obj.speak()

class Animal:
    def speak(self):
        print('动物叫，但不知道时哪种动物叫')

class Dog(Animal):
    def speak(self):
        print('小狗叫。。。')

class Cat(Animal):
    def speak(self):
        print('小猫叫。。。')


class Car:
    def speak(self):
        print('滴滴滴。。。')




# d = Dog()
# d.speak()
# c = Cat()
# c.speak()
# car=Car()
# car.speak()

start(Dog())
start(Cat())
start(Car())