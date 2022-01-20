# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
from flask import abort, jsonify, Flask, request, Response
import json
import xml.sax
import pymysql
import random
app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

#连接数据库
# evo_conn = pymysql.connect(host="172.31.238.143",user="root", password="root123", charset="utf8")
# evo_cursor = evo_conn.cursor()
# evo_cursor.execute('SELECT id FROM evo_wes_basic.basic_sku WHERE state = "effective" AND sn_enabled = 0 ORDER BY rand() LIMIT 3;')
# a = evo_cursor.fetchall()
# sku_id = random.choice(a)[0]
# print(sku_id)

taskss ='<?xml version="1.0" encoding="UTF-8" ?> \
<header /> \
<body> \
<success>true</success> \
<code>{}</code> \
<message>Return success</message> \
</body>'



tasksl = {
	"header": {
		"requestId": "5f643ec0",
		"timestamp": "2019-06-01 12:28:38",
		"version": "2.0"
	},
	"body": {
		"success":'true',
		"code": "OK",
		"message": "业务请求处理成功",
		"data": {
			"event": {}
		}
	}
}


@app.route('/sce-openapi-webapp/fh/authorized/workRequest', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_taskss():
    get_value = request.get_data()
	#get_value2 = request.get_data
    print(get_value)
    return jsonify(taskss)

@app.route('/apicallback/quicktron/dcs/job', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_taska():
	evo_conn = pymysql.connect(host="172.31.238.143", user="root", password="root123", charset="utf8")
	evo_cursor = evo_conn.cursor()
	evo_cursor.execute(
		'SELECT id FROM evo_wes_basic.basic_sku WHERE state = "effective" AND sn_enabled = 0 ORDER BY rand() LIMIT 3;')
	a = evo_cursor.fetchall()
	sku_id = random.choice(a)[0]
	get_value = json.loads(request.get_data(as_text=True))
	print(get_value)
	return jsonify({
	"header": "{}".format(sku_id),
	"body": {
		"success":'true',
		"code": "OK",
		"message": "业务请求处理成功",
		"data": {
			"event": {}
		}
	}
})



@app.route('/apicallback/quicktron/wms/job', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/sl
def get_tasksl():
    get_value = json.loads(request.get_data(as_text=True))
    print(get_value)
    return jsonify(tasksl)

if __name__ == '__main__':
    app.run(host = '172.31.248.64',port = 1234,debug = True)
# if __name__ == '__main__':
#     app.run(host = '172.31.252.42',port = 1234,debug = True)