# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 :
# 开发工具 : PyCharm
from xuexi.getpoint import select_map

#sql = 'select json_data from evo_rcs.basic_map where map_state="OnLine"'

result = select_map("172.31.236.92")
stronge = result[2]
list_result = []
print(stronge)
f = open("point.txt", "a")
for i in stronge:
    a = i + "\n"
    list_result.append(a)
print(list_result)
f.writelines(list_result)
f.close()