# _*_ coding : UTF-8 _*_
# 开发团队 : 火星团队
# 开发人员 : hcx
# 开发时间 : 2020/10/10 15:12
# 文件名称 : 
# 开发工具 : PyCharm
import logging
import json
import pymysql
from venv import logger


def select_map(service_ip):
    """
    :param sql: 分析地图，拿出地图所有的点位
    :return: 返回多个点位类型 元祖
    """
    try:
        evo_conn = pymysql.connect(host="{}".format(service_ip),  user="root", password="root123",
                                   cursorclass=pymysql.cursors.DictCursor, charset="utf8")
        cursor = evo_conn.cursor()
        sql_1 = 'select json_data from evo_rcs.basic_map where map_state="OnLine"'
        cursor.execute(sql_1)
    except Exception as e:
        logger.error(e)
    else:
        json_data = cursor.fetchone()
        str_data = json_data.get("json_data")
        zone_list = json.loads(str_data).get("zoneList")
        #print(zone_list)
        pd_work_point_list = []
        storage_point_list = []
        online_point_list = []
        entrance_point_list = []
        forbidden_point_list = []
        path_point_list = []
        other_device_point_list = []
        for i in zone_list:
            for pointList in i.get("pointList"):
                if pointList.get("pointType") == "BUCKET_PUTDOWN_WORKING":
                    pd_work_point_list.append(pointList.get("pointCode"))

                elif pointList.get("pointType") == "STORAGE":
                    storage_point_list.append(pointList.get("pointCode"))

                elif pointList.get("pointType") == "STATION_WORKING":
                    online_point_list.append(pointList.get("pointCode"))

                elif pointList.get("pointType") == "BUCKET_ENTRANCE":
                    entrance_point_list.append(pointList.get("pointCode"))

                elif pointList.get("pointType") == "FORBIDDEN":
                    forbidden_point_list.append(pointList.get("pointCode"))

                elif pointList.get("pointType") == "PATH":
                    path_point_list.append(pointList.get("pointCode"))

                elif pointList.get("pointType") == "OTHER_DEVICE":
                    other_device_point_list.append(pointList.get("pointCode"))
        for i in zone_list:
            for pointList in i.get("relationList"):
                if pointList.get("relationType") == "DEVICE_INTERACTION":
                    other_device_point_list.append(pointList.get("pointCode"))
        cursor.close()
        evo_conn.close()
        return pd_work_point_list, online_point_list, storage_point_list, path_point_list, \
               entrance_point_list, other_device_point_list, forbidden_point_list




