# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
import json
import os
from datetime import timedelta
from flask import Flask,request
from flask_cors import CORS
from gevent import monkey,pywsgi
monkey.patch_all()
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['SECRET_KEY'] = os.urandom(24) #设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7) #设置session的保存时间。
UPLOAD_FOLDER='upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/tciOutSide_v1.0/AGV/GetAbnormalInfor',methods=['POST','GET','OPTIONS'],strict_slashes=False)
def workbin_report():
    get_value = json.loads(request.get_data(as_text=True))
    print(get_value)
    return_msg={}
    return_msg['code']=200
    return_msg['success'] = True
    return json.dumps(return_msg)

if __name__ == '__main__':
    # app.run(debug=True,threaded=True, port=9990,host='0.0.0.0') host为本地ip及端口号配置
    host = '172.31.251.192'
    port = 9999
    print(host+':'+str(port))
    server = pywsgi.WSGIServer((host,port),app)
    server.serve_forever()