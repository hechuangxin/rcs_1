
# a={"agv":"creey001","bucket":"T-5","name":"木头人","age":"123"}

# # print(a["agv"])       #打印key值为"agv"  获取对应的value
# a["sex"]="nan"        #插入key值为"sex"  value值为"nan"
# a["sex"]="nv"          #修改key值为"sex"  value值为"nv"
# print(a)
# a["jobtype"]=["youxian",1,"99"]     #插入key值为"jobtype"  value值为["youxian",1,"99"]
# print(a)
# # print(a.pop("bucket"))     #提取
# a.pop("name")      #把 “ name” 提取之后打印    删除指定值
# print(a)
# a.popitem()     #随机删除一个key值
# print(a)
# a.clear()
# print(a)  #删除列表里所有的值
# print(a.items())
# print(a.items())      #key值和value值组合到一起
# print(a.keys())       #获取所有的key值
# print(a.values())       #获取所有的value值

# b={"我是","最帅的","ren","我是"}
# print(b)
# b=["我是","最帅的","ren","我是"]
# print(b)
# b=set(["我是","最帅的","ren","我是"])
# print(b)
# print(8//5)    #整除
# print(8%5)     #取余
# print(2**3)     #2的3次方
# print(100.1-0.2)
from decimal import Decimal
# print(Decimal('1.235')-Decimal('0.1'))    #精确到很高的位置  ， 要写成字符串形式
# print(type(Decimal('1.235') - Decimal('0.1')))     #判断类型  <class 'decimal.Decimal'>
# print(Decimal('56.6') - Decimal('10') == Decimal('46.6'))
# print(8//5==1)               #打印 8除5整除结果是否为1
#比较运算    <        >            <=         >=             ==          !=
#           小于    大于      小于等于        大于等于        等于         不等于
# print(1 >= 0.1)
# print(1 <= 2)
# print(1 <= 1)
# print(4 >= 2)
# print(3 != 1)
# a,b=1,2
# print(a)
# print(b)
#  and    并且    同时为真
# print(1==1 and 2==2)       #返回  True
# print(3==3 and 4==5)        #返回  False
# #   or     只要有一个为真就返回True
# print("qwe"=="qwe" or "asd"=="fdaasd")
# # not   取相反的意思
# print(not 1==1 and 2==2)
# # in  在什么什么里面，not in  不在什么什么里面
# print(2 in [1,2,3])
# print("001" not in {"agv":"001","bucket":"t-001"})     #只针对value
# a=' 123 '
# b=a.replace('3','2')
# print(b)
# a = ('aa',11)
# b = ('bb',22)
# c = [('cc',33)]
# d = {}
# a_key = a[0]
# # print(a_key)
# d[a_key] = a[1]
# print(d)                     #把a ， b， c， 插入到 d 字典里面
# d[b[0]] = b[1]
# print(d)
# # c_key = c[0]
# # print(c_key)
# # c1=c_key[0]
# # print(c1)
# d[c[0][0]] = c[0][1]
# print(d)
# x = [a, b, c[0]]            # 使用dict方法
# print(dict(x))

#if   elif   else

# a=1
# if type(a) == int :
#     pass
# elif type(a) == str :
#     print("我最帅")
# else:
#     print("我要学习")
# print('今天是美好的一天')
# a=[11,21,432,7654,763,876765,234,2]
# for b in a:
#     print(b)

# a={"agv":"creey001","bucket":"T-5","name":"木头人","age":"123"}
#
# for b in a.values():
#     print('hahaha:{}'.format(b))               #把输出格式化
# for c in a.items():
#     print(c)             #打印获取到的字典
# for d in a .keys():
#     print(d)            #打印获取到的所有的key值
# a = 0
# while(a <=10):
#     print('hahaahahaaha')
#     print(a)
#     a+= 1
# print('钓鱼去')
# b = 0
# while True:
#     print('天气晴朗')
#     print(b)
#     if b == 10:
#         print('今天是个好日子')
#         break            #退出循环
#     b+= 1
# print('已退出循环')

# a = [1,2,3,4,5,6,7,8,9]
# b = [1,2,3,4,5,6,7,8,9]
# for c in a:
#     for d in b:
#         print('{} * {} = {}'.format(c,d,c*d),end='\t')

# for q in range(1,10):
#     for w in range(1,10):
#         if w <= q :
#             print('{}*{}={}'.format(w,q,w*q),end='\t')
#     print()

# def a(x,y):
#     c = y+1
#     d = x*2
#     return c,d            #return返回值
# print(a(4,7))


# def user_info(A,b,p):
#     print('agvcode:{}'.format(A))
#     print('bucket:{}'.format(b))                      #TODO：没懂
#     print('poindcode:{}'.format(p))
#
#
# user_info('1232','t-5','fsadfsdf')
# user_info(p='fsadfsdf',A='1232',b='t-5')         #贴上标签可以无序，关键字参数

# def a(qw,er,*c):
#     b=2
#     d=qw+er+b
#     for n in c:
#         d+=n
#     return d
# m=[3,4,5]
# print(a(1,2,*m))

# def a(b,c,*args,**kwargs):
#     print(args)
#     print(kwargs)
# a(1,2,3,4,zx='hhh',qw='qwe')


#当函数没有被调用之前，函数的定义顺序没有关系
name = '晓峰'
def dalao():
    global name
    name = name + '彼'
    print('{} is dalao'.format(name))
print(dalao())
print(name)




