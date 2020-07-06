'''
    sql = 'select * from zh_stu limit 5;'
    res = op_mysql(sql = sql)
    response = json.dumps(res,ensure_ascii=False)
    logger.info("接收任务回报下发ok")
    return response #return只能返回字符串
    '''