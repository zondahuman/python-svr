# -*- coding:utf-8 -*-
# !/usr/bin/env python

# -*- coding: UTF-8 -*-
# 来源：疯狂的蚂蚁的博客www.server110.com总结整理
import MySQLdb as mdb
import sys


def selectSubmitInfo(application_sn, task_type, application_source):
    print "selectSubmitInfo-------------start--------------"
    #获得mysql查询的链接对象
    con = mdb.connect('172.16.2.112', 'heika_dev', 'heika_dev@qwe321', 'rrd_verify')
    with con:
        #获取连接上的字典cursor，注意获取的方法，
        #每一个cursor其实都是cursor的子类
        cur = con.cursor(mdb.cursors.DictCursor)
        #执行语句不变
        sql = "SELECT * FROM verify_application_submit_info where application_sn="+"'"+application_sn+"'"+" and task_type= "+"'"+task_type+"'"+" and application_source= "+"'"+application_source+"'"+""
        print "sql= " , sql
        cur.execute(sql)
        #获取数据方法不变
        rows = cur.fetchall()
        print "rows= " , rows
        #遍历数据也不变（比上一个更直接一点）
        for row in rows:
            #这里，可以使用键值对的方法，由键名字来获取数据
            verify_appl_status_id = row["verify_appl_status_id"]
            print "verify_appl_status_id= " , verify_appl_status_id
            return verify_appl_status_id
    print "selectSubmitInfo-------------end--------------"

def selectStatus(verify_appl_status_id):
    print "selectStatus-------------start--------------"
    #获得mysql查询的链接对象
    con = mdb.connect('172.16.2.112', 'heika_dev', 'heika_dev@qwe321', 'rrd_verify')
    with con:
        #获取连接上的字典cursor，注意获取的方法，
        #每一个cursor其实都是cursor的子类
        cur = con.cursor(mdb.cursors.DictCursor)
        #执行语句不变
        sql = "SELECT * FROM verify_application_status where id=%s"%verify_appl_status_id
        print "sql= " , sql
        cur.execute(sql)
        #获取数据方法不变
        rows = cur.fetchall()
        print "rows= " , rows
        #遍历数据也不变（比上一个更直接一点）
        for row in rows:
            #这里，可以使用键值对的方法，由键名字来获取数据
            application_id = row["application_id"]
            print "application_id= " , application_id
            return application_id
    print "selectStatus-------------end--------------"

def selectLimit(application_id):
    print "selectLimit-------------start--------------"
    #获得mysql查询的链接对象
    con = mdb.connect('172.16.2.112', 'heika_dev', 'heika_dev@qwe321', 'rrd_verify')
    with con:
        #获取连接上的字典cursor，注意获取的方法，
        #每一个cursor其实都是cursor的子类
        cur = con.cursor(mdb.cursors.DictCursor)
        sql = "SELECT * FROM verify_application_limit where step='ONE' and application_id= "+"'"+application_id+"'"+""
        print "sql= " , sql
        #执行语句不变
        cur.execute(sql)
        #获取数据方法不变
        rows = cur.fetchall()
        #遍历数据也不变（比上一个更直接一点）
        for row in rows:
            #这里，可以使用键值对的方法，由键名字来获取数据
            input = row["input"]
            print "input= " , input
            return input
    print "selectLimit-------------end--------------"

def createFileByIdNo():
    print "createFileByIdNo-------------start--------------"
    for i in range(111111111111101501, 111111111111116067):
        application_sn = str(i)
        task_type = str(i)
        application_source = "RRD"
        idNo = str(i)
        print "application_sn= ", application_sn, ",task_type=", task_type, ",application_source=", application_source, ",idNo=", idNo
        status_id = selectSubmitInfo(application_sn, task_type, application_source)
        if status_id:
            application_id = selectStatus(status_id)
            if application_id:
                input = selectLimit(application_id)
                if input:
                    file_name = "/opt/app/script/application/%s"%str(idNo)+".txt"
                    print "file_name= " , file_name
                    file=open(file_name,'w')    # r只读，w可写，a追加
                    file.write(input+'\n')
                    file.close()
    print "createFileByIdNo-------------end--------------"

if __name__ == "__main__":
    createFileByIdNo()