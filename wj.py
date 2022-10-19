# f=open('/Users/Fan/Desktop/test.txt','w+')
# f.write('Panpan')
#
# f=open('/Users/Fan/Desktop/test.txt','r+')
# f.write('Hello!')
#
# f=open('/Users/Fan/Desktop/test.txt','a+')
# f.write(' World!')
# f.close()

# f_name = '/Users/Fan/Desktop/test.txt'
# f = None
# try:
#     f=open(f_name)
#     print('open test.txt')
#     content=f.read()
#     print(content)
# except FileNotFoundError as e:
#     print('FileNotFoundError')
# except OSError as e:
#     print('OSError')
# finally:
#     if f is not None:
#         f.close()
#         print('close test.txt')

#复制文件
f_name = '/Users/Fan/Desktop/test.txt'
# f = open(f_name)
# d=f.read()
# print(d)
with open(f_name,'r',encoding='utf-8')as f:
    lines=f.readlines()
    copy_f_name='/Users/Fan/Desktop/cope_test.txt'
    with open(copy_f_name,'w',encoding='gbk')as copy_f:
        copy_f.writelines(lines)
print(open(copy_f_name, 'r').read())


#复制图片
p_name ='/Users/Fan/Desktop/正.jpg'
with open(p_name,'rb')as f:  #'rb'读取二进制文件
    b=f.read()
    copy_p_name='/Users/Fan/Desktop/copy_正.jpg'
    with open(copy_p_name,'wb')as copy_f:  #'wb'写二进制文件
        copy_f.write(b)






