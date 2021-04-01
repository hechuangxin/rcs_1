# a = int(input("请输入中奖号码："))
# b = int(input("猜个数："))
# if a == 123:
#     print("可以领奖")
#
# else:
#     print("没中奖")

# number = int(input("请输入商品销量："))
# if number >= 1000:
#     print("销量为 A ")
# elif number >= 500:
#     print("销量为B")
# elif number >= 300:
#     print("销量为C")
# else:
#     print("销量惨淡")
"""
年龄在18岁以上可以开车，
在70岁以上不可以开车
"""
# age = int(input("请输入年龄:"))
# if age >= 18:
#     if age <= 70:
#         print("可以开车,扶好方向盘")
# else:
#     print("回家吃饭")

# a = input()
# print(type(a))
# if type(a) == str:
#     print("只能为数字")
#     if type(a) == float:
#         print("不能为小数")
#         if type(a) == int:
#             print("支付成功")

# for i in ["明日","科技","与你","同行"]:
#     print(i)

"""计算0+1+2+3+4......+100的值"""
# b=0
# for a in range(1,101):
#     b=b+a
# print(b)



# password = 0
# a = 1
# while a < 7:
#     b = int(input("请输入密码："))
#     if b == password:
#         print("密码正确")
#         a = 7
#     else:
#         print("密码输入错误，已输入",a,"次")
#     a = a+1
# if a==7:
#     print("已冻结")
# total = 99
# for number in range(1,100):
#     if number % 7 == 0:
#         continue
#     else:
#         string = str(number)
#         if string.endswith('7'):
#             continue
#     total = total - 1
# print(total)

"""
1. 如果有钱，则可以上车
    2. 上车后，如果有空座，可以坐下
    上车后，如果没有空座，则站着等空座位
如果没钱，不能上车
"""
# 假设用 money = 1 表示有钱, money = 0表示没有钱; seat = 1 表示有空座，seat = 0 表示没有空座
# money = int(input('输入金额：'))
# seat = 1
# if money >= 1:
#     print("有钱可以上车")
#     if seat == 1:
#         print("可以上车坐下")
#     else:
#         print("站着")
# else:
#     print("没钱")

# name = ['邓肯','吉诺比利','帕克']
# sing = ['石佛','妖刀','跑车']
# dictionary = dict(zip(name,sing))
# print(dictionary)

# a = dict(b = 1,d = 2 )
# print(a)
# print(a['d'])
# #根据get方法获取值，当没有key值时返回默认值：“没有值”
# print('c的值是：',a.get('c','没有值'))
# a.clear()
# print(a)

# aa= {'qq':'1234555','明日科技':'5435235','无语':'65632'}
# #提取key值
# #print(aa.pop('qq'))
# for b in aa.items():
#     print(b)
# for c in aa.keys():
#     print(c)
# for d in aa.values():
#     print(d)


# for a in range(1,10):
#     for b in range(1,a+1):
#         print('{}*{}={}'.format(b,a,a*b),end='\t')
#     print()


# a = dict((('德玛西亚之力','盖伦'),('弗雷尔卓德','布隆')))
# print(a)
# #添加一个元素
# a['n']='1'
# print(a)
# #替换n的值
# a['n']='2'
# print(a)
# #删除一个元素
# # del a['n']
# # print(a)
# if 'n' in a:
#     del a['n']
# print(a)
# set1 = set('初听不知曲中意')
# print(set1)
# pf = set(['1','2','3'])
# print('a的值有：',pf)
def a(x,y):
    for q in range(x,y):
        for w in range(x,q+1):
            print('{}*{}={}'.format(w,q,q*w))
a(1,3)












