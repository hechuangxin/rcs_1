import requests
import pymysql
import random
import json
import time
import uuid

headers = {
    "Content-Type": "application/json",
    "charset": "utf-8",
}
evo_conn = pymysql.connect(host="172.31.238.16",port=30082,user="root", password="123456", charset="utf8")
evo_cursor = evo_conn.cursor()
list = ['9001_kckq_WHBtmm','9001_kckq_B5sp7r']

#list = ['6001_kckq_tnzQah', '6001_kckq_AXN3MZ', '6001_kckq_M8pTAX', '6001_kckq_nChwhs', '6001_kckq_2ey8KK']

def back_bucket():
    robotjobID_list = {}
    while True:
        station = random.choice(list)
        evo_cursor.execute("SELECT robot_job_id from evo_rcs.robot_job where state = 'ENTER_STATION' and target_point = %s ;", (station,))
        evo_conn.commit()
        result = evo_cursor.fetchone()
        if not result:
            time.sleep(0.1)
            continue
        robotjobId = result[0]
        if robotjobID_list.get(station, None) == robotjobId:
            continue
        back_data = {
                          "robotJobId" : "{}".format(robotjobId),
                          "warehouseId":"1"
                        }
        robotjobID_list[station] = robotjobId
        response = requests.post(url='http://172.31.238.16:31038/api/rcs/standardized/operation/notice',
                                 data=json.dumps(back_data), headers=headers)
        if json.loads(response.text).get('msg', False) == 'success':
            time.sleep(1)
            print("货架{}到工作站，当前任务序号:{}, 开始下发回库任务".format(robotjobId, back_data['robotJobId']))
            break
        else:
            time.sleep(1)


def create_job():
    order = 1
    for i in range(order):
        evo_cursor.execute('select bucket_code,point_code from evo_basic.basic_bucket where enabled="1" and point_code !="-1" and point_code is not NULL;')
        result = evo_cursor.fetchall()
        bucket_code = random.choice(result)[0]
        tostation_data = {
                          "bucketCode":"{}".format(bucket_code),
                          "checkCode": 1,
                          "endPoint": "{}".format(random.choice(list)),
                          "endArea":"",
                          "jobPriority": 9,
                          "jobPriorityType": 1,
                          "letDownFlag": "offline",
                          "robotJobId": "A{}".format(uuid.uuid4()),
                          "workFace":"2",
                          "transportEntityType": "BUCKET",
                          "warehouseId":1,
                          "containerCode":"",
                          "bucketSlotId":"",
                          "targetBucketSlotId":"",
                          "deadline":"",
                          "agvType":"",
                          "zoneCode":"kckq",
                          "agvEndPoint":"",
                          "robotJobGroupId":"",
                          "agvCode":""
                        }
        response = requests.post(url='http://172.31.238.16:31038/api/rcs/standardized/robot/job/submit',
                                 data=json.dumps(tostation_data), headers=headers)
        if json.loads(response.text).get('msg') == 'success':
            print("第{}个出库任务下发成功".format(i + 1))
            print(response.text)
            time.sleep(0.1)
        else:
            print("第{}个出库任务下发失败".format(i + 1))
            print(response.text)

while True:
    create_job()
    time.sleep(60)
    # back_bucket()
    # time.sleep(60)