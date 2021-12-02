# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
#盘点单
list2 = []
for i in range(1,4001):
    id = str(i) + '${uuid}'
    skuCode = '${sku_code1_' + str(i) + '}'
    packCode = '${sku_code1_' + str(i) + '}-${sku_code1_' + str(i) + '}'
    json1 = {
				"ownerCode": "${ownerCode}",
				"skuCode": "{}".format(skuCode),
				"lotAtt01": "1",
				"lotAtt02": "",
				"lotAtt03": "",
				"lotAtt04": "",
				"lotAtt05": "",
				"lotAtt06": "",
				"lotAtt07": "",
				"lotAtt08": "",
				"lotAtt09": "",
				"lotAtt10": "",
				"lotAtt11": "",
				"lotAtt12": ""
			}

    list2.append(json1)

print(list2)
