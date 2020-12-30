# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
from flask import abort, jsonify, Flask, request, Response
import json

app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

taskss = {
    "code": 0,
    "msg": "OK",
    "data": {
        },
    "traceId": "dp1r"
}

tasksl = {
    "code": 0,
    "data": {
        "waybillStatus": "10",
        "deliveryAbbreviationAddress": "深圳",
    },
}

@app.route('/apicallback/quicktron/equipment.access.request', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_taskss():
    get_value = json.loads(request.get_data(as_text=True))
    print(get_value)
    return jsonify(taskss)

@app.route('/apicallback/quicktron/robotjob.report', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/sl
def get_tasksl():
    get_value = json.loads(request.get_data(as_text=True))
    print(get_value)
    return jsonify(tasksl)

if __name__ == '__main__':
    app.run(host = '172.31.224.49',port = 1234,debug = True)