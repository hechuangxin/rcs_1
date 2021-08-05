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
# app.config['JSON_AS_ASCII'] = False
# task01 ='<?xml version="1.0" encoding="UTF-8" ?> \
# <header /> \
# <body> \
# <success>{}</success> \
# <code>{}</code> \
# <message>Return success</message> \
# </body>'
#
# task01 = task01.format('aaaa','bbb')
#
# print(task01 )


@app.route('/sce-openapi-webapp/fh/authorized/workRequest', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_task01():
    evo_conn = pymysql.connect(host="172.31.238.143", user="root", password="root123", charset="utf8")
    evo_cursor = evo_conn.cursor()
    evo_cursor.execute(
        'SELECT * FROM evo_wes_basic.basic_sku WHERE state = "effective" AND sn_enabled = 0 ORDER BY rand() LIMIT 3;')
    a = evo_cursor.fetchall()
    sku_id = random.choice(a)[0]
    sku_code = random.choice(a)[2]
    get_value = request.get_data()
    print(get_value)
    return ('<?xml version="1.0" encoding="UTF-8" ?> \
<header /> \
<body> \
<success>{}</success> \
<code>{}</code> \
<message>Return success</message> \
</body>'.format(sku_id,sku_code))





if __name__ == '__main__':
    app.run(host = '172.31.219.121',port = 1234,debug = True)