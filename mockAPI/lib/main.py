# import tools #使用时，需要用tools.op_mysql()
from lib.tools import op_mysql  #使用时，直接用op_mysql()
from flask import Flask, render_template
from loguru import logger
import pdb
# 以上两种方式都可以

import flask,json #python的轻量级的开发框架
# 接口，后台服务的开发
# 在浏览器运行http://127.0.0.1:8080/get_user即可，或者其他访问接口的方式
server = flask.Flask(__name__) #__name__当前文件名，把咱们这个app python当做一个server


  #浏览器输出bt_stu表中前5条的数据
@server.route('/ge_user', methods=['get', 'post']) #将下面函数变成一个接口
def get_all_user():
    sql = 'select * from zh_stu limit 5;'
    res = op_mysql(sql=sql)
    response = json.dumps(res, ensure_ascii=False)
    logger.info("接收任务回报下发ok")
    return response  # return只能返回字符串




# 浏览器输入用户id、姓名,插入数据到数据库stu表，
@server.route('/get_user',methods=['post']) #代码支持什么类型的接口
def add_user():
    '''
    #from-data格式
    JobId = flask.request.values.get('id')
    houseId = flask.request.values.get('u')
    '''
    JobId = flask.request.get_json('')
    dict_id = json.dumps(JobId)
    print(dict_id)

    return json.dumps(dict_id,ensure_ascii=False)

