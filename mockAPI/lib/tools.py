import pymysql
from conf import setting

# 1、操作mysql
def op_mysql(sql):
    conn = pymysql.connect(host=setting.MYSQL_HOST,user= setting.USER,
                           password=setting.PASSWORD,
                           port=setting.PORT,
                           charset='utf8',
                           db=setting.DB)
    cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #判断是否需要commit，根据select update delete insert的类型
    cur.execute(sql)
    sql_start = sql[:6].upper()# select不区分大小写,取前6位转换成大写
    if sql_start == 'SELECT':
        res = cur.fetchall()
    else:
        conn.commit()
        res = 'ok'
    cur.close()
    conn.close()
    return res