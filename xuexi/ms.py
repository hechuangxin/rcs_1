# _*_ coding : UTF-8 _*_
from flask import abort, jsonify, Flask, request, Response
import json

app = Flask(__name__)
# 增加配置，支持中文显示
app.config['JSON_AS_ASCII'] = False

taskss = {
    "code": 0,
    "msg": "OK",
    "success": "true",
    "data": {
        },
    "traceId": "dp1r"
}

tasksl = {
        "header": {
                      "requestId": "5f643ece-dc53-4d55-8e5f-d1e2dfd6a6d0",
                      "timestamp": "2019-06-01 12:28:38",
                      "version": "2.0"
                  },
        "body":{
      "success": "true",
      "code": "OK",
      "message": "业务请求处理成功",
      "data": {
        "event":{
        "success": "true",
        "code": "OK"
                }
              }
                }
                    }

@app.route('/apicallback/quicktron/equipment.access.request', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/ss
def get_taskss():
    get_value = json.loads(request.get_data(as_text=True))
    get_value.encoding = 'utf-8'
    print(get_value)
    return jsonify(taskss)




@app.route('/maapi/in', methods=['GET','POST'])            #访问网址：http://127.0.0.1:6868/task/sl
def get_tasksl():
    get_value = json.loads(request.get_data(as_text=True))
    print(get_value)
    return jsonify(tasksl)


if __name__ == '__main__':
    app.run(host='172.31.249.114', port=1234, debug=True)