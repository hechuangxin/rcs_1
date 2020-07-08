# import keyword
# keyword.kwlist
# A='每天进步一点点，赚最多的钱'
# print(type(A))
# print(len(A))


# print(A[0:3])   #打印索引从0到2的字符
# print(A[2:5])   #打印索引从2到4的字符
# print(A[0:])    #打印索引从0开始至结束
# print(A[4:])    #打印索引从4到结束的字符
# print(A[:6])    #打印索引从0到5的字符
# print(A[:])     #打印全部
# print(A[::2])   #打印步长为2所有的字符：每进一点赚多钱
# print(A[333:])   #切片超出长度不会报错
# print(A[222])    #索引超出超度会报错：string index out of range
# print(A[1:2])

# print(A[::-1])
# print(A[-1:-5:-1])  #打印索引从-1到-5的字符，不包含-5
# print(A[-1:-6:-2])  #打印索引从-1到-6的字符，步长为-2

# a=input("请输入名字")
# b=input("请输入年龄")
# c=input("请输入性别")
# print("""
# name:{}
# age:{}
# xingbie:{}
# """.format(a,b,c))
# print("""
# name:{2}
# age:{0}
# xingbie:{1}
# """.format(a,b,c))
# print("""
# name:{2}
# age:{0}
# sex:{1}""".format(a,b,c))
# abc= "qwer"
# print(abc.upper())     #打印为大写
# a2="QWER"
# print(a2.lower())        #打印为小写
# print(a2.upper().lower())     #打印为小写
# a3="QWERTyuio"
# print(a3.swapcase())     #大小写转换打印
#
# # find查找，如果找不到就会返回-1
# # 当找到指定元素，显示第一个索引位置
# # 必须是连续的字符
# a4=a3.find("RT")
# print(a4)
# print(len(a3))
# print(a3.find("o"))
# print(a3.index("u"))
# # index和find类似
# # 找不到元素时会报错  ValueError
# # IndexError  索引错误
# a5=a3.index("Rt")
# print(a5)
# a6="11112222333"
# a7=a6.replace("1","444")   #把 1 替换成4
# a8=a6.replace("1","444",2)   #把 1 替换成4,只替换两个 1
# print(a6)
# print(a8)
# print(a6.count("2"))    #打印，统计元素为2的数量
# print(a6.replace("3","5"))
# print(a6.replace("3","5",2))
#
a_11="我是,"
a_22="最帅,"
a_33="的,"
# a_44="123".join([a_11,a_22,a_33])     #join拼接
# print(a_44)
# print(a_44.split("123,"))      #切割123
print("一群人".join([a_11,a_33,a_22]).split("的"))

#
# b_1=" 我是最帅的我 "
# print(b_1.strip(" 我"))    #去掉左右两边的 “ 我”
# print(b_1.rstrip(" 我"))    #去掉右两边的 “ 我”
# print(b_1.lstrip("我 "))    #去掉左两边的 “ 我”
#
b_2="334556674524"
print(b_2.isdigit())     #isdigit判断是否为正整数 ，不是：False，是正整数：True

#
# abc=["123","木头人"]
# abc.append("我是")     #添加一个 “我是” 到末尾 #只能添加单个
# print(abc)
#
# abc.extend(["我们","都是"])     #添加一个 "我们","都是" 到末尾
# print(abc)
#
# abc.insert(1,"哈哈哈")        #添加 “哈哈哈” 到索引为 1 的位置
# print(abc)
#
# abc.remove("木头人")      #删除列表中 “木头人”
# print(abc)
#
# abc.pop(1)      #删除索引为 1 位置的元素
# abc.pop()        #pop没有指定索引的时候删除末尾的最后一个
# print(abc)
#
# abc[2]=666    #修改索引为2的位置的  为 666
# print(abc)
#
# #第一种逆序
# abc.reverse()     #倒叙排列
# print(abc)
#
# #第二种逆序，需赋值给一个新的变量
# m=abc[::-1]
# print(m)
#
# c_1=[3,666,7,564,98,444,7867]
# c_1.sort()        #正序排列
# print(c_1)
# c_1.sort(reverse=True)     #倒叙排列
# print(c_1)
#
# #哈哈哈哈哈哈哈哈啊哈
# print(c_1)
# a="qwewqe"