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

if __name__ == '__main__':
    app.run(host = '172.31.219.121',port = 1234,debug = True)
#工作提供接口
@app.route('/sce-openapi-webapp/fh/authorized/workRequest', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_task01():
    get_value = request.get_data()
    print(get_value)
    return jsonify(task01)

task01 ='<?xml version="1.0" encoding="UTF-8" ?> \
<header /> \
<body> \
<success>true</success> \
<code>{}</code> \
<message>Return success</message> \
</body>'

#工作提供握手接口
@app.route('/sce-openapi-webapp/fh/authorized/workRequest', methods=['GET','POST'])
def get_task02():
    get_value = request.get_data()
    print(get_value)
    return jsonify(task02)

task02 = '<?xml version="1.0" encoding="UTF-8" ?> \
<header /> \
<body> \
<success>true</success> \
<code>{}</code> \
<message>Return success</message> \
</body>'

#唯品会工作反馈接口
@app.route('/sce-openapi-webapp/fh/authorized/workRequest', methods=['GET','POST'])
def get_task03():
    get_value = request.get_data()
    print(get_value)
    return jsonify(task03)

task03 = '<?xml version="1.0" encoding="UTF-8" ?> \
<header /> \
<body> \
<success>true</success> \
<code>{}</code> \
<message>Return success</message> \
</body>'

#唯品会交接箱提供接口
@app.route('/sce-openapi-webapp/fh/authorized/workRequest', methods=['GET','POST'])
def get_task04():
    get_value = request.get_data()
    print(get_value)
    return jsonify(task04)

task04 = '<?xml version="1.0" encoding="UTF-8" ?> \
<header /> \
<body> \
<success>true</success> \
<code>{}</code> \
<message>Return success</message> \
</body>'


#唯品会交接箱提供握手接口
@app.route('/sce-openapi-webapp/fh/authorized/workRequest', methods=['GET','POST'])
def get_task05():
    get_value = request.get_data()
    print(get_value)
    return jsonify(task05)

task05 = '<?xml version="1.0" encoding="UTF-8" ?> \
<header /> \
<body> \
<success>true</success> \
<code>{}</code> \
<message>Return success</message> \
</body>'

#唯品会交接箱反馈接口
@app.route('/sce-openapi-webapp/fh/authorized/workRequest', methods=['GET','POST'])
def get_task06():
    get_value = request.get_data()
    print(get_value)
    return jsonify(task06)

task06 = '<?xml version="1.0" encoding="UTF-8" ?> \
<header /> \
<body> \
<success>true</success> \
<code>{}</code> \
<message>Return success</message> \
</body>'

#唯品会事件提供接口
@app.route('/sce-openapi-webapp/fh/authorized/workRequest', methods=['GET','POST'])
def get_task07():
    get_value = request.get_data()
    print(get_value)
    return jsonify(task07)

task07 = '<?xml version="1.0" encoding="UTF-8" ?> \
<header /> \
<body> \
<success>true</success> \
<code>{}</code> \
<message>Return success</message> \
</body>'

#唯品会事件提供握手接口
@app.route('/sce-openapi-webapp/fh/authorized/workRequest', methods=['GET','POST'])
def get_task07():
    get_value = request.get_data()
    print(get_value)
    return jsonify(task07)

task07 = '<?xml version="1.0" encoding="UTF-8" ?> \
<header /> \
<body> \
<success>true</success> \
<code>{}</code> \
<message>Return success</message> \
</body>'











