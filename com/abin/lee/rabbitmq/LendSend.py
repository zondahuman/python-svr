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
{"data":{"additionalMaterialList":[{"comment":"用户合照","name":"用户合照","path":"https://api.xiaofen.net.cn//static/attachments/20174731/83177c78-5af8-4396-8c6f-e1f1451a5a19_20170331164731.jpg"}],"applicationSn":"021490949228211899","applicationSource":"YM","contactList":[{"mobile":"13085568205","name":"a"},{"mobile":"13225742090","name":"A"}],"emergencyContactList":[{"mobile":"18771925269","name":"孙汉林","relation":"父母"}],"loanInfo":{"loanAmount":20000,"loanPurpose":"医美","orgAddress":"长宁区武夷路447号","orgCode":"YMSHA0011","orgCoefficient":"0.5","orgName":"上海美仑医疗美容门诊部有限公司","orgType":"--","product":"鼻材料硅胶假体取出","projTotalAmount":456780,"projectDetails":[{"projName":"鼻材料硅胶假体取出","projPrice":4000}]},"positionList":[{"createTime":"1490949724000","eventType":"LOGIN","ipAddress":"116.231.67.186, 58.222.41.13","lat":31.21431144524996,"lng":121.4163902889893},{"createTime":"1490947101000","eventType":"REGISTER","ipAddress":"116.231.67.186, 58.222.41.13","lat":0,"lng":0}],"questionnaire":{"orderSn":"021490949228211899","questions":[{"answer":"1","id":1,"list":[{"id":1,"seqId":1,"title":"是"},{"id":2,"seqId":2,"title":"否"}],"title":"是否渠道来客"},{"answer":"4","id":2,"list":[{"id":3,"seqId":1,"title":"公关"},{"id":4,"seqId":2,"title":"主播"},{"id":5,"seqId":3,"title":"网红"},{"id":6,"seqId":4,"title":"其他自由职业"},{"id":7,"seqId":5,"title":"服务业"},{"id":8,"seqId":6,"title":"媒体体育娱乐"},{"id":9,"seqId":7,"title":"学生"},{"id":10,"seqId":8,"title":"家庭主妇（一般）"},{"id":11,"seqId":9,"title":"家庭主妇（富裕）"},{"id":12,"seqId":10,"title":"其他"}],"title":"职业范畴"},{"answer":"17","id":3,"list":[{"id":13,"seqId":1,"title":"校园"},{"id":14,"seqId":2,"title":"网红直播"},{"id":15,"seqId":3,"title":"美容院"},{"id":16,"seqId":4,"title":"夜店"},{"id":17,"seqId":5,"title":"模特经纪"},{"id":18,"seqId":6,"title":"微整工作室"}],"title":"渠道来源"},{"answer":"20","id":4,"list":[{"id":19,"seqId":1,"title":"否"},{"id":20,"seqId":2,"title":"是且另1家"},{"id":21,"seqId":3,"title":"是且另2家"},{"id":22,"seqId":4,"title":"是且另3家及以上"}],"title":"是否申请了别家"},{"answer":"23","id":5,"list":[{"id":23,"seqId":1,"title":"否"},{"id":24,"seqId":2,"title":"是且低于10000"},{"id":25,"seqId":3,"title":"是且低于20000"},{"id":26,"seqId":4,"title":"是且低于30000"},{"id":27,"seqId":5,"title":"是且低于50000"},{"id":28,"seqId":6,"title":"是且高于50000"}],"title":"么么贷通过情况"},{"answer":"31","id":6,"list":[{"id":29,"seqId":1,"title":"优秀"},{"id":30,"seqId":2,"title":"良好"},{"id":31,"seqId":3,"title":"一般"},{"id":32,"seqId":4,"title":"较差"},{"id":33,"seqId":5,"title":"极差"}],"title":"客户基本情况"},{"answer":"36","id":7,"list":[{"id":34,"seqId":1,"title":"优秀"},{"id":35,"seqId":2,"title":"良好"},{"id":36,"seqId":3,"title":"一般"},{"id":37,"seqId":4,"title":"较差"},{"id":38,"seqId":5,"title":"极差"}],"title":"对项目了解程度"},{"answer":"39","id":8,"list":[{"id":39,"seqId":1,"title":"否"},{"id":40,"seqId":2,"title":"是且之前是微整"},{"id":41,"seqId":3,"title":"是且之前是手术"}],"title":"是否复购客户"},{"answer":"42","id":9,"list":[{"id":42,"seqId":1,"title":"否"},{"id":43,"seqId":2,"title":"复购第二次"},{"id":44,"seqId":3,"title":"复购第三次"},{"id":45,"seqId":4,"title":"复购第四次及以上"}],"title":"复购次数"},{"answer":"46","id":10,"list":[{"id":46,"seqId":1,"title":"是"},{"id":47,"seqId":2,"title":"否"}],"title":"是否有信用卡"},{"answer":"49","id":11,"list":[{"id":48,"seqId":1,"title":"是"},{"id":49,"seqId":2,"title":"否"}],"title":"是否预警"}]},"taskType":"12","userBasicInfo":{"age":30,"blackBoxId":"860439036314051","callHistoryJobId":"c000e83a-6836-4652-8513-7f38a12e7b40","company":"","consumerCoefficient":"0.5776190476190476","domain":"媒体/娱乐/体育","schoolName":"麻省理工学院","cardNo":"6217003130004852741","educationDegree":"JUNIOR_COLLEGE","email":"200617718@qq.com","gender":"FEMALE","homeAddress":"武汉市江岸区惠济路42号4栋1单元1楼3号","houseCity":"205","houseProvince":"18","idCardAddress":"武汉市江岸区惠济路42号4栋1单元1楼3号","idCardPhotoBack":"https://api.xiaofen.net.cn//static/attachments/20173331/99c200ab-485f-4872-9735-7c5da8cbdba9_file.jpg","idCardPhotoFront":"https://api.xiaofen.net.cn//static/attachments/20173231/be652261-0ccd-4432-8f79-cb712079846e_file.jpg","idCardPhotoHand":"https://api.xiaofen.net.cn//static/attachments/20173331/7a1c7dde-857a-4a81-9490-51ff67221991_file.jpg","idNo":"420102198702062445","idNoValidityDate":"2036-03-07","job":"","jobName":"婚庆司仪","loanAppNumber":0,"mobile":"13886052211","platform":"ANDROID","realName":"孙菁","userKey":466}},"sendTime":1490950262268,"sequenceId":0,"source":"YM","type":"AUDIT_REQUEST","uniqKey":"021490949228211899"}    """
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
    realName = '杨正祥'
    #从    111111111111100000
    #到    111111111111116067
    # ###
    # for i in range(111111111111100000, 111111111111100100):
    # for i in range(111111111111100100, 111111111111101000):
    for i in range(100000000000000000, 100000000000000001):
    # for i in range(111111111111101000, 111111111111116067):
    # for i in range(111111111111103000, 111111111111116067):
    # for i in range(222222222222203000, 222222222222203001):
        idNo = str(i)
        uniqKey = idNo
        # taskType = sys.argv[1]
        taskType = idNo
        print "idNo="+idNo
        send(idNo, taskType, uniqKey, realName)