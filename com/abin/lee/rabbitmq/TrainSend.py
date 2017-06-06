# -*- coding:utf-8 -*-
# !/usr/bin/env python
import threading

import pika
import json
import uuid
import random
from com.abin.lee.util import CharacterUtil,UuidUtil,NumberUtil,IdNoUtil,MobileUtil

def send(idNo, taskType, uniqKey, realName, userKey, mobile):
    credentials = pika.PlainCredentials('guest', 'guest')
    # 这里可以连接远程IP，请记得打开远程端口
    parameters = pika.ConnectionParameters('172.16.2.145', 15671, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    body="""
{"data":{"additionalMaterialList":[{"comment":"用户合照","name":"用户合照","path":"https://api.xiaofen.net.cn//static/attachments/20171516/ff2b57b6-89b9-4a9e-b3a3-15dffbca9a55_20170416181516.jpg"}],"applicationSn":"0214923366828369045111","applicationSource":"TL","contactList":[{"mobile":"13806709573","name":"若 依"},{"mobile":"13625733063","name":"朱忠良"}],"emergencyContactList":[{"mobile":"13625733063","name":"朱忠良","relation":"父母"}],"loanInfo":{"loanAmount":48000,"loanPhase":6,"loanPurpose":"教育培训","repayMode":"OTHERPAYBACK","repayInterest":432.05,"repayBalance":1500.54},"positionList":[{"createTime":"1492337302000","eventType":"LOGIN","ipAddress":"223.104.5.230, 223.111.213.20","lat":31.19952597141875,"lng":121.4648794575539},{"createTime":"1492336460000","eventType":"REGISTER","ipAddress":"223.104.5.230, 223.111.213.19","lat":31.199526,"lng":121.464879}],"taskType":"1","userBasicInfo":{"age":27,"blackBoxId":"B33145E4-969B-432A-9EE6-7E5BDC76CBB9","callHistoryJobId":"","educationDegree":"MIDDLE_SCHOOL","email":"396654970@qq.com","gender":"FEMALE","houseProvince":"广东省","houseCity":"汕头市","homeAddress":"浙江省嘉善县惠民街道大泖村河墩2号","idCardPhotoBack":"https://api.xiaofen.net.cn//static/attachments/20175616/ad8f59b1-d54e-4609-944a-17175643fcf2_file.jpg","idCardPhotoFront":"https://api.xiaofen.net.cn//static/attachments/20175616/0902935a-efc7-4c20-b58d-7e9d0f843f9a_file.jpg","idCardPhotoHand":"https://api.xiaofen.net.cn//static/attachments/20175816/e127dbdf-5eab-47be-949d-50bb4a0c2ba5_file.jpg","idNo":"330421198909021820","idNoValidityDate":"2035-10-04","mobile":"13645836311","platform":"IOS","realName":"朱静","schoolName":"普林斯顿学院","userKey":778,"student":1,"className":"大数据培训","qq":"123456","educationJobId":"2caf0c5f-17a1-4ddf-94a0-dea7f7d103d7"},"relationInfo":{"institution":{"instBand":"M1","instName":"穆迪评级","instCode":"C919"},"branch":{"branchName":"加州大学伯克利分校","branchCode":"B747","branchProvince":"广东省","branchCity":"深圳市"},"schoolInfo":{"admissionBatch":"第一批次","nineEightFive":"1","twoOneOne":"0"}}},"sendTime":1492337882097,"sequenceId":0,"source":"TL","type":"AUDIT_REQUEST","uniqKey":"0214923366828369045111"}
    """
    body = json.loads(body)
    body['uniqKey'] = uniqKey
    body['data']['applicationSn'] = uniqKey
    body['data']['taskType'] = taskType
    body['data']['userBasicInfo']['idNo'] = idNo
    body['data']['userBasicInfo']['realName'] = realName
    body['data']['userBasicInfo']['userKey'] = userKey
    body['data']['userBasicInfo']['mobile'] = mobile

    content = json.dumps(body)
    print "Sent is : %s" %content

    channel.basic_publish(exchange='',routing_key='audit.request.queue',body=content)
    print " [x] Sent %s" %body
    connection.close()

def assemble():
     # realName = '杨正祥'
    # idNo = '533527198909210238'
    # realName = '倪瑶博'
    # idNo = '110101197606085635'
    # realName = '马克龙'
    # idNo = '110101198606250113'
    realName = CharacterUtil.createName()
    idNo = IdNoUtil.create_id_no()
    # idNo = '110101198606250113'
    userKey = UuidUtil.loanUuidAll()
    uniqKey = UuidUtil.loanUuid15()
    mobile = MobileUtil.createMobile()
    # taskType = sys.argv[1]
    taskType = 1
    taskType = NumberUtil.randomNumber(5, 10)
    print "idNo="+idNo
    send(idNo, taskType, uniqKey, realName, userKey, mobile)

def concurrency():
    threads = []
    for num in range(0, 5):
        # threadName = 't' + num
        threadName = threading.Thread(target=assemble,args=())
        threads.append(threadName)
    print "threads", threads
    for thread in threads:
        thread.setDaemon(True)
        thread.start()

if __name__ == "__main__":
   # assemble()
   #  concurrency()
    threads = []
    thread_count = 5
    for num in range(0, thread_count):
        # threadName = 't' + num
        threadName = threading.Thread(target=assemble,args=())
        # threadName.setDaemon(True)
        # threadName.daemon = True
        threads.append(threadName)

    print "threads", threads
    # for thread in threads:
    #     # thread.setDaemon(True)
    #     thread.start()
    for i in range(0, thread_count):
        threads[i].daemon = True
        threads[i].start()