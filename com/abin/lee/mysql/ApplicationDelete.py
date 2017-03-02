#! /usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "abin"
import pymysql
import json


def deleteUserContact(application_id):
    print "deleteUserContact-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "DELETE FROM verify_application_user_contact where application_id="+"'"+application_id+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    print "deleteUserContact-------------end--------------"


def deleteUserEmergencyContact(application_id):
    print "deleteUserEmergencyContact-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "DELETE FROM verify_application_user_emergency_contact where application_id="+"'"+application_id+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    print "deleteUserEmergencyContact-------------end--------------"

def deleteUserInfo(application_id):
    print "deleteUserInfo-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "DELETE FROM verify_application_user_info where application_id="+"'"+application_id+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    print "deleteUserInfo-------------end--------------"


def deleteLimit(application_id):
    print "deleteLimit-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "DELETE FROM verify_application_limit where application_id="+"'"+application_id+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    print "deleteLimit-------------end--------------"


def deletePbcRelation(application_id):
    print "deletePbcRelation-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "DELETE FROM verify_pbc_relation where application_id="+"'"+application_id+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    print "deletePbcRelation-------------end--------------"


def deleteStatus(application_id):
    print "deleteStatus-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "DELETE FROM verify_application_status where application_id="+"'"+application_id+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    print "deleteStatus-------------end--------------"

def deleteSchedule(application_id):
    print "deleteSchedule-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "DELETE FROM verify_application_schedule where application_id="+"'"+application_id+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    print "deleteSchedule-------------end--------------"


def deleteUserMobileRegion(application_id):
    print "deleteUserMobileRegion-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "DELETE FROM verify_application_user_mobile_region where application_id="+"'"+application_id+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    print "deleteUserMobileRegion-------------end--------------"


def deleteUserPositionn(application_id):
    print "deleteUserPositionn-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "DELETE FROM verify_application_user_position where application_id="+"'"+application_id+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    print "deleteUserPositionn-------------end--------------"


def deleteSubmitInfo(application_sn, task_type, application_source):
    print "deleteSubmitInfo-------------start--------------"
    conn = pymysql.connect(host='172.16.2.112', port=3306, user='heika_dev', passwd='heika_dev@qwe321', db='rrd_verify')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "DELETE FROM verify_application_submit_info where application_sn="+"'"+application_sn+"'"+" and task_type= "+"'"+task_type+"'"+" and application_source= "+"'"+application_source+"'"+""
    print "sql= " , sql
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()
    print "deleteSubmitInfo-------------end--------------"

def call():
    print "call-------------start--------------"
    for i in range(111111111111100001, 111111111111103000):
    # for i in range(111111111111103000, 111111111111106067):
    # for i in range(111111111111106067, 111111111111109067):
    # for i in range(111111111111109067, 111111111111112067):
    # for i in range(111111111111112067, 111111111111116067):
        param = str(i)
        application_sn = str(param)
        task_type = str(param)
        application_source = "RRD"
        idNo = param
        print "application_sn= ", application_sn, ",task_type=", task_type, ",application_source=", application_source, ",idNo=", idNo
        application_id = application_source + '_'+ application_sn + "_" + task_type
        print "application_id= " , application_id
        # deleteUserContact(application_id)
        # deleteUserInfo(application_id)
        # deleteLimit(application_id)
        # deletePbcRelation(application_id)
        # deleteUserEmergencyContact(application_id)
        deleteUserMobileRegion(application_id)
        deleteUserPositionn(application_id)
        # deleteSubmitInfo(application_sn, task_type, application_source)
        print "call-------------end--------------"

if __name__ == "__main__":
   call()



