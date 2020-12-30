# -*- coding=utf-8 -*-
"""
此模块用以通过地图获取工作站移位货架点位信息
"""
import json

import pymysql

db = pymysql.connect(host='172.31.238.13', user='root',port=32457, password='123456', charset="utf8")
cursor = db.cursor()
sql = 'select json_data from evo_rcs.basic_map where map_state="OnLine"'
cursor.execute(sql)
mapDate =cursor.fetchone()[0]
dicMapDate = json.loads(mapDate)
print(dicMapDate)
zoneList = dicMapDate.get("zoneList")
pdworkPointList = []
stoPointList = []
onlinePointList = []
offlinedict = dict()
onlinedict = dict()
storagedict=dict()
for i in zoneList:
    for pointList in i.get("pointList"):
        if pointList.get("pointType")=="BUCKET_PUTDOWN_WORKING":
            pdworkPointList.append(pointList.get("pointCode"))

        if pointList.get("pointType")=="STORAGE":
            stoPointList.append(pointList.get("pointCode"))

        if pointList.get("pointType")=="STATION_WORKING":
            onlinePointList.append(pointList.get("pointCode"))

offlinedict["BUCKET_PUTDOWN_WORKING"] = pdworkPointList
storagedict["STORAGE"] = stoPointList

onlinedict["STATION_WORKING"] = pointList.get("pointCode")

def getofflinedict():
    '''
    :return: 离线工作站点位
    '''
    return offlinedict

def getonlinedict():
    '''
    :return: 在线工作站点位
    '''
    return onlinedict
def getstoragedict():
    '''
    :return: 存储点位
    '''
    return storagedict

db.close()