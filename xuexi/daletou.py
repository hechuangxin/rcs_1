# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
"""
输入注数生成大乐透号码
红球取值范围1-36，篮球1-12
"""
import random


class GreatLotto:
    """
    需要一个生成次数count
    """
    global result  # 声明全局变量
    result = []

    def __init__(self, count):
        self.count = count

    def randoms(self):
        """
        :return: 返回传入次数的随机彩票号码(返回的是一个整体列表)
        """
        for i in range(self.count):
            for j in range(7):
                if j <= 4:
                    index1 = random.randrange(1, 36)
                    result.append(index1)
                if j > 4:
                    index1 = random.randrange(1, 13)
                    result.append(index1)
        return result  # 返回生成结果

    def start(self):
        """
        :return: 根据传入的次数判断列表取值的开始数
        """
        for l in range(self.count):
            if l < 1:
                two = l
            else:
                two = l * 7
            yield two  # yield是生成器,将每次循环生成的结果储存(如果使用了return会结束循环，导致只能执行一次)

    def ends(self, rer):
    #根据传入的次数判断列表取值的结束数
        for k in range((len(rer) + 1) // 7):  # 小数不能循环我们用地板除
            one = (k + 1) * 7
            yield one  # yield是生成器,将每次循环生成的结果储存(如果使用了return会结束循环，导致只能执行一次)


if __name__ == '__main__':
    num = int(input("请输入需要生成的注数："))
    Great = GreatLotto(num)  # 实例化GreatLotto 并将输入的次数传入
    lists = Great.randoms()  # 得到返回的生成结果
    zips = zip(Great.start(), Great.ends(lists))  # 压缩两个函数 使for循环可以同时循环两个对象
    for m, n in zips:  # 遍历两个函数的生成器
        print(lists[m:n])