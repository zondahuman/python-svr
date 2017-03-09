# -*- coding:utf-8 -*-
#!/usr/bin/python
# __author__ = "abin"
import paramiko
import pymysql
import json
import encodings.idna

DATABASE_HOST='10.10.12.140'
DATABASE_PORT=3306
DATABASE_USER='select'
DATABASE_PWD='aaaaaaaa'
DATABASE_NAME='verify'

SSH_HOST='116.213.205.158'
SSH_PORT=11111
SSH_USER='lee'
SSH_PWD='lee'

def findApplication():
    print "findApplication-------------start--------------"
    conn = pymysql.connect(host=DATABASE_HOST, port=DATABASE_PORT, user=DATABASE_USER, passwd=DATABASE_PWD, db=DATABASE_NAME)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select sta.application_id, sta.current_verify_status, sta.create_time, sta.update_time from verify_application_status sta, verify_application_limit lim , verify_application_schedule sch where sta.current_verify_status='SYSTEM_REJECT' and lim.step='ONE' and lim.creditType='2' and sta.application_id = lim.application_id and sta.application_id = sch.application_id and sch.one=1 and sch.whole=0 "
    print "sql= " , sql
    cursor.execute(sql)

    # 获取剩余结果的第一行数据
    row_1 = cursor.fetchone()
    print 'row_1= ', row_1
    list = []
    if row_1:
        application_id = row_1["application_id"]
        print "application_id= ", application_id
        list.append(application_id)

    # row_2 = cursor.fetchmany(3)

    # 获取剩余结果所有数据
    # row_3 = cursor.fetchall()

    conn.commit()
    cursor.close()
    conn.close()
    print "findApplication-------------end--------------"
    return list  # 获取剩余结果前n行数据



if __name__ == '__main__':
    # paramiko.util.log_to_file("filename.log")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(SSH_HOST, SSH_PORT, SSH_USER, SSH_PWD)
    sql = "select sta.application_id, sta.current_verify_status, sta.create_time, sta.update_time from verify_application_status sta, verify_application_limit lim , verify_application_schedule sch where sta.current_verify_status='SYSTEM_REJECT' and lim.step='ONE' and lim.creditType='2' and sta.application_id = lim.application_id and sta.application_id = sch.application_id and sch.one=1 and sch.whole=0 "
    print "sql= " , sql
    stdin, stdout, stderr = ssh.exec_command("mysql -h172.16.2.112 -P3306 -uheika_dev -pheika_dev@qwe321 rrd_verify -e '"+sql+"'")
    print "stdout= ",stdout.readlines()
    print "stdin= ",stdin
    print "stderr= ",stderr

    # list = findApplication()
    # print list
    ssh.close()