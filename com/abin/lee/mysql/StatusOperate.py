#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "TKQ"
import pymysql
import json


def selectSubmitInfo(application_sn, task_type, application_source):
    print "selectSubmitInfo-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "SELECT * FROM verify_application_submit_info where application_sn="+"'"+application_sn+"'"+" and task_type= "+"'"+task_type+"'"+" and application_source= "+"'"+application_source+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    # 获取剩余结果的第一行数据
    row_1 = cursor.fetchone()
    print 'row_1= ', row_1
    verify_appl_status_id = ''
    if row_1:
        verify_appl_status_id = row_1["verify_appl_status_id"]
        print "verify_appl_status_id= ", verify_appl_status_id

    # row_2 = cursor.fetchmany(3)

    # 获取剩余结果所有数据
    # row_3 = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    print "selectSubmitInfo-------------end--------------"
    return verify_appl_status_id  # 获取剩余结果前n行数据


def call():
    param = 222222222222203000
    application_sn = str(param)
    task_type = str(param)
    application_source = "RRD"
    idNo = param
    print "application_sn= ", application_sn, ",task_type=", task_type, ",application_source=", application_source, ",idNo=", idNo
    status_id = selectSubmitInfo(application_sn, task_type, application_source)
    print "status_id= ", status_id

if __name__ == "__main__":
   call()



