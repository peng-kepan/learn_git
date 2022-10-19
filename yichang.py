class PanpanException(Exception):#自定义异常
    def __init__(self,message):
        super().__init__(message)

i=input('请输入一个数字：')
n=8888
try:
    result =n/int(i)
    print(result)
except ZeroDivisionError as e:
    #print('不能除以0，异常：{}'.format(e))
    raise PanpanException('不能除以0')
except ValueError as e:
   #print('....{}'.format(e))
   raise PanpanException('输入的无效数字')
finally:#释放资源
    print('释放资源...')





