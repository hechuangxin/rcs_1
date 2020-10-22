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
total = 99
for number in range(1,100):
    if number % 7 == 0:
        continue
    else:
        string = str(number)
        if string.endswith('7'):
            continue
    total = total - 1
print(total)