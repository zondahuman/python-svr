# -*- coding:utf-8 -*-
# !/usr/bin/env python
import pika
import json
import uuid
import random

def send(idNo, taskType, uniqKey, realName, userKey):
    credentials = pika.PlainCredentials('guest', 'guest')
    # 这里可以连接远程IP，请记得打开远程端口
    parameters = pika.ConnectionParameters('172.16.2.145', 15671, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    body="""
{"sendTime":1489747985863,"uniqKey":"224ijnr0No7zml4J1","source":"RRD","type":"AUDIT_REQUEST","sequenceId":0,"data":{"applicationSn":"224ijnr0No7zml4J1","applicationSource":"RRD","taskType":52,"description":"首次进件","loanInfo":{},"userBasicInfo":{"callHistoryJobId":"2ef210ec-37c5-4b11-9f92-e01c8f624628","userKey":"0bb6c3ad28355d4d7479f276673fface","idNo":"370285199110282926","realName":"王萌","gender":"FEMALE","idCardPhotoFront":"http://172.16.1.76//Nirvana-2017-03-17/ID_CARD_POSITIVE_224_2017-03-17_18-47-44_avatar.png","idCardPhotoBack":"http://172.16.1.76//Nirvana-2017-03-17/ID_CARD_NEGATIVE_224_2017-03-17_18-47-56_avatar.png","idNoValidityDate":"2023-08-22","mobile":"18513622928","reserveMobile":"18513622928","email":"123456@qq.com","blackBoxId":"ewogICJ0b2tlbklkIiA6ICJyZW5yZW5kYWkxNWFkYWY4NDA4Zi03YjMyZDQyMGQxOWM5NzgzNWU2OTYxYjI3ZTM3ODAwNyIsCiAgIm9zIiA6ICJpT1MiLAogICJwcm9maWxlVGltZSIgOiA0NDcsCiAgInZlcnNpb24iIDogIjIuMS40Igp9","houseProvince":"2","houseCity":"36","houseDistrict":"377","houseAddress":"默默","homeAddress":"山东省莱西市院上镇朱西庄村198号","platform":"IOS","cardNo":"6217000010042791759","educationDegree":"COLLEGE","graduateDate":"2014-06-01"},"emergencyContactList":[{"name":"登录账号","mobile":"15678100724","relation":"其他"},{"name":"畅悦秀","mobile":"15010695238","relation":"其他"}],"contactList":[{"name":"畅悦秀","mobile":"15010695238"},{"name":"登录账号","mobile":"15678100724"}],"positionList":[{"createTime":1489747689000,"eventType":"APPLY_LOAN","ipAddress":"10.20.1.97","lng":"116.33719815643","lat":"39.99973988301","province":"","city":"","position":"北京市海淀区中关村东路1号"}],"facePlusPlus":{"confidence":8.01,"thresholds_1e_3":8.01,"thresholds_1e_4":8.01,"thresholds_1e_5":8.01,"thresholds_1e_6":8.01,"mask_confidence":8.01,"screen_replay_confidence":8.01,"mask_threshold":8.01,"synthetic_face_confidence":8.01,"synthetic_face_threshold":8.01,"screen_replay_threshold":8.01,"face_replaced":6},"competitionProductsList":[{"appPackageName":"包名1","appName":"RRD1","updateDayDiff":1430236800},{"appPackageName":"包名2","appName":"RRD2","updateDayDiff":1470236800}]}}
    """
    body = json.loads(body)
    body['uniqKey'] = uniqKey
    body['data']['applicationSn'] = uniqKey
    body['data']['taskType'] = taskType
    body['data']['userBasicInfo']['idNo'] = idNo
    body['data']['userBasicInfo']['realName'] = realName
    body['data']['userBasicInfo']['userKey'] = userKey

    content = json.dumps(body)
    print "Sent is : %s" %content

    channel.basic_publish(exchange='',routing_key='audit.request.queue',body=content)
    print " [x] Sent %s" %body
    connection.close()

if __name__ == "__main__":
    # realName = '杨正祥'
    # idNo = '533527198909210238'
    # realName = '倪瑶博'
    # idNo = '110101197606085635'
    realName = '马克龙'
    idNo = '110101198606250113'
    unique = str(uuid.uuid1());
    uniqKey = unique.replace('-','')
    userKey = unique.replace('-','')
    offset = random.randint(10, 15)
    uniqKey = uniqKey[0:offset]
    # taskType = sys.argv[1]
    taskType = random.randint(1, 200)
    print "idNo="+idNo
    send(idNo, taskType, uniqKey, realName, userKey)