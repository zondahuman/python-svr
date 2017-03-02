# -*- coding:utf-8 -*-
# !/usr/bin/env python
import pika
import json

def send(idNo, taskType, uniqKey, realName):
    credentials = pika.PlainCredentials('guest', 'guest')
    # 这里可以连接远程IP，请记得打开远程端口
    parameters = pika.ConnectionParameters('172.16.2.145', 15671, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    body="""
        {"sendTime":1488354977583,"uniqKey":"9Czh2Hek","source":"RRD","type":"AUDIT_REQUEST","sequenceId":0,"data":{"applicationSn":"9Czh2Hek","applicationSource":"RRD","taskType":1,"description":"\u9996\u6b21\u8fdb\u4ef6","loanInfo":{},"userBasicInfo":{"callHistoryJobId":"eded6afb-14f5-4c0f-81a1-63eb6735d8f3","userKey":"65bab4ec428f3f0159e95c0e60910dac","idNo":"370285199110282926","realName":"\u738b\u840c","gender":"FEMALE","idCardPhotoFront":"https:\/\/loan.renrendai.com\/\/Nirvana-2017-03-01\/ID_CARD_POSITIVE_9_2017-03-01_15-08-03_avatar.png","idCardPhotoBack":"https:\/\/loan.renrendai.com\/\/Nirvana-2017-03-01\/ID_CARD_NEGATIVE_9_2017-03-01_15-08-13_avatar.png","idNoValidityDate":"2023-08-22","mobile":"18513622928","reserveMobile":"18513622928","email":"wangmeng@qq.com","blackBoxId":"ewogICJ0b2tlbklkIiA6ICJ1Y3JlZGl0MTVhODhhYjY3NDMtYjc4NWQ0ZGEyYmRmZTQ5MDMwNmI1ZGY3MDBiOGJjMWUiLAogICJvcyIgOiAiaU9TIiwKICAicHJvZmlsZVRpbWUiIDogMTk1LAogICJ2ZXJzaW9uIiA6ICIyLjEuNCIKfQ==","houseProvince":"2","houseCity":"36","houseDistrict":"377","houseAddress":"\u4e1c\u57ce\u533a","homeAddress":"\u5c71\u4e1c\u7701\u83b1\u897f\u5e02\u9662\u4e0a\u9547\u6731\u897f\u5e84\u6751198\u53f7","platform":"ANDROID","cardNo":"6217000010042791759","educationDegree":"COLLEGE","graduateDate":"2014-06-04"},"emergencyContactList":[{"name":"\u8463\u6dd1\u7389","mobile":"17710390240","relation":"\u5176\u4ed6"},{"name":"\u675c\u658c","mobile":"13910393653","relation":"\u5176\u4ed6"}],"contactList":[{"name":"\u6731\u53d4\u53d4","mobile":"18765453977"},{"name":"\u5e84\u4e91\u9e4f","mobile":"15653508119"}],"positionList":[{"createTime":1488352111000,"eventType":"APPLY_LOAN","ipAddress":"117.21.168.89","lng":"116.33710536909","lat":"39.999782459818","province":"","city":"","position":"\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u4e2d\u5173\u6751\u4e1c\u8def1\u53f7"}]}}
    """
    body = json.loads(body)
    body['uniqKey'] = uniqKey
    body['data']['applicationSn'] = uniqKey
    body['data']['taskType'] = taskType
    body['data']['userBasicInfo']['idNo'] = idNo
    body['data']['userBasicInfo']['realName'] = realName

    content = json.dumps(body)
    print "Sent is : %s" %content

    # body = "{\"sendTime\":1488354977583,\"uniqKey\":" + uniqKey + ",\"source\":\"RRD\",\"type\":\"AUDIT_REQUEST\",\"sequenceId\":0,\"data\":{\"applicationSn\":" + uniqKey + ",\"applicationSource\":\"RRD\",\"taskType\":"+taskType+",\"description\":\"\u9996\u6b21\u8fdb\u4ef6\",\"loanInfo\":{},\"userBasicInfo\":{\"callHistoryJobId\":\"eded6afb-14f5-4c0f-81a1-63eb6735d8f3\",\"userKey\":\"65bab4ec428f3f0159e95c0e60910dac\",\"idNo\":"+"'"+idNo+"'"+",\"realName\":"+"'"+realName+"'"+",\"gender\":\"FEMALE\",\"idCardPhotoFront\":\"https:\/\/loan.renrendai.com\/\/Nirvana-2017-03-01\/ID_CARD_POSITIVE_9_2017-03-01_15-08-03_avatar.png\",\"idCardPhotoBack\":\"https:\/\/loan.renrendai.com\/\/Nirvana-2017-03-01\/ID_CARD_NEGATIVE_9_2017-03-01_15-08-13_avatar.png\",\"idNoValidityDate\":\"2023-08-22\",\"mobile\":\"18513622928\",\"reserveMobile\":\"18513622928\",\"email\":\"wangmeng@qq.com\",\"blackBoxId\":\"ewogICJ0b2tlbklkIiA6ICJ1Y3JlZGl0MTVhODhhYjY3NDMtYjc4NWQ0ZGEyYmRmZTQ5MDMwNmI1ZGY3MDBiOGJjMWUiLAogICJvcyIgOiAiaU9TIiwKICAicHJvZmlsZVRpbWUiIDogMTk1LAogICJ2ZXJzaW9uIiA6ICIyLjEuNCIKfQ==\",\"houseProvince\":\"2\",\"houseCity\":\"36\",\"houseDistrict\":\"377\",\"houseAddress\":\"\u4e1c\u57ce\u533a\",\"homeAddress\":\"\u5c71\u4e1c\u7701\u83b1\u897f\u5e02\u9662\u4e0a\u9547\u6731\u897f\u5e84\u6751198\u53f7\",\"platform\":null,\"cardNo\":\"6217000010042791759\",\"educationDegree\":\"COLLEGE\",\"graduateDate\":\"2014-06-04\"},\"emergencyContactList\":[{\"name\":\"张三\",\"mobile\":\"17710390240\",\"relation\":\"\u5176\u4ed6\"},{\"name\":\"张三1\",\"mobile\":\"13910393653\",\"relation\":\"\u5176\u4ed6\"}],\"contactList\":[{\"name\":\"张三2\",\"mobile\":\"18610281472\"}],\"positionList\":[{\"createTime\":1488352111000,\"eventType\":\"APPLY_LOAN\",\"ipAddress\":\"117.21.168.89\",\"lng\":\"116.33710536909\",\"lat\":\"39.999782459818\",\"province\":\"\",\"city\":\"\",\"position\":\"\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u4e2d\u5173\u6751\u4e1c\u8def1\u53f7\"}]}}"
    channel.basic_publish(exchange='',routing_key='audit.request.queue',body=content)
    print " [x] Sent %s" %body
    connection.close()


if __name__ == "__main__":
    realName = '李国强'
    #从    111111111111100000
    #到    111111111111116067
    #
    #
    #
    # ###
    # for i in range(111111111111100100, 111111111111116067):
    # for i in range(111111111111103000, 111111111111116067):
    for i in range(222222222222203000, 222222222222203001):
        idNo = str(i)
        uniqKey = idNo
        # taskType = sys.argv[1]
        taskType = idNo
        print "idNo="+idNo
        send(idNo, taskType, uniqKey, realName)