# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
#出库单下发
# list2 = []
# for i in range(1,2501):
#     id = str(i) + '${uuid}'
#     skuCode = '${sku_code1_' + str(i) + '}'
#     json1 = {
#         "id": "{}".format(id),
#         "ownerCode": "${ownerCode}",
#         "skuCode": "{}".format(skuCode),
#         "frozenFlag": 'false',
#         "quantity": "${__Random(1,10,)}",
#         "lotAtt01": "",
#         "lotAtt02": "",
#         "lotAtt03": "",
#         "lotAtt04": "",
#         "lotAtt05": "",
#         "lotAtt06": "",
#         "lotAtt07": "",
#         "lotAtt08": "",
#         "lotAtt09": "",
#         "lotAtt10": "",
#         "lotAtt11": "",
#         "lotAtt12": "",
#         "extendedProperties": {}
#       }
#
#     list2.append(json1)
#
# print(list2)
#出库单取消
list2 = []
for i in range(1,51):
    id = str(i) + '${uuid}'
    pick = '${pick_' + str(i) + '}'
    json1 = ["{}".format(pick)
]

    list2.append(json1)

print(list2)