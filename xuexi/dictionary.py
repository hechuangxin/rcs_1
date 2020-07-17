from decimal import Decimal
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
# print(Decimal('1.235')-Decimal('0.1'))    #精确到很高的位置
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
print("001" not in {"agv":"001","bucket":"t-001"})


