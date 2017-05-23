# -*- coding:utf-8 -*-
# !/usr/bin/env python
import pika
import json
import time
import random
from com.abin.lee.util import CharacterUtil,NumberUtil,IdNoUtil

def send(idNo, taskType, uniqKey, realName, userKey):
    credentials = pika.PlainCredentials('guest', 'guest')
    # 这里可以连接远程IP，请记得打开远程端口
    parameters = pika.ConnectionParameters('172.16.2.145', 15671, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    body="""
        {"data":{"additionalMaterialList":[{"comment":"用户合照","name":"用户合照","path":"https://api.xiaofen.net.cn//static/attachments/20171516/ff2b57b6-89b9-4a9e-b3a3-15dffbca9a55_20170416181516.jpg"}],"applicationSn":"0214923366828369045111","applicationSource":"YM","contactList":[{"mobile":"13806709573","name":"若 依"},{"mobile":"13625733063","name":"朱忠良"}],"emergencyContactList":[{"mobile":"13625733063","name":"朱忠良","relation":"父母"}],"loanInfo":{"loanAmount":48000,"loanPurpose":"医美","orgAddress":"上海市黄浦区瑞金南路341号西北室","orgCode":"YMSHA0038","orgCoefficient":"0.9","orgName":"上海宏津企业管理有限公司锦坤门诊部","orgType":"--","product":"脂肪填充脂肪隆胸","projTotalAmount":45000,"projectDetails":[{"projName":"脂肪填充脂肪隆胸","projPrice":45000,"projNum":5}]},"positionList":[{"createTime":"1492337302000","eventType":"LOGIN","ipAddress":"223.104.5.230, 223.111.213.20","lat":31.19952597141875,"lng":121.4648794575539},{"createTime":"1492336460000","eventType":"REGISTER","ipAddress":"223.104.5.230, 223.111.213.19","lat":31.199526,"lng":121.464879}],"questionnaire":{"orderSn":"021492336682836904","questions":[{"answer":"2","id":1,"list":[{"id":1,"seqId":1,"title":"是"},{"id":2,"seqId":2,"title":"否"}],"title":"是否渠道来客"},{"answer":"3","id":2,"list":[{"id":3,"seqId":1,"title":"公关"},{"id":4,"seqId":2,"title":"主播"},{"id":5,"seqId":3,"title":"网红"},{"id":6,"seqId":4,"title":"其他自由职业"},{"id":7,"seqId":5,"title":"服务业"},{"id":8,"seqId":6,"title":"媒体体育娱乐"},{"id":9,"seqId":7,"title":"学生"},{"id":10,"seqId":8,"title":"家庭主妇（一般）"},{"id":11,"seqId":9,"title":"家庭主妇（富裕）"},{"id":12,"seqId":10,"title":"其他"}],"title":"职业范畴"},{"answer":"16","id":3,"list":[{"id":13,"seqId":1,"title":"校园"},{"id":14,"seqId":2,"title":"网红直播"},{"id":15,"seqId":3,"title":"美容院"},{"id":16,"seqId":4,"title":"夜店"},{"id":17,"seqId":5,"title":"模特经纪"},{"id":18,"seqId":6,"title":"微整工作室"}],"title":"渠道来源"},{"answer":"20","id":4,"list":[{"id":19,"seqId":1,"title":"否"},{"id":20,"seqId":2,"title":"是且另1家"},{"id":21,"seqId":3,"title":"是且另2家"},{"id":22,"seqId":4,"title":"是且另3家及以上"}],"title":"是否申请了别家"},{"answer":"23","id":5,"list":[{"id":23,"seqId":1,"title":"否"},{"id":24,"seqId":2,"title":"是且低于10000"},{"id":25,"seqId":3,"title":"是且低于20000"},{"id":26,"seqId":4,"title":"是且低于30000"},{"id":27,"seqId":5,"title":"是且低于50000"},{"id":28,"seqId":6,"title":"是且高于50000"}],"title":"么么贷通过情况"},{"answer":"29","id":6,"list":[{"id":29,"seqId":1,"title":"优秀"},{"id":30,"seqId":2,"title":"良好"},{"id":31,"seqId":3,"title":"一般"},{"id":32,"seqId":4,"title":"较差"},{"id":33,"seqId":5,"title":"极差"}],"title":"客户基本情况"},{"answer":"34","id":7,"list":[{"id":34,"seqId":1,"title":"优秀"},{"id":35,"seqId":2,"title":"良好"},{"id":36,"seqId":3,"title":"一般"},{"id":37,"seqId":4,"title":"较差"},{"id":38,"seqId":5,"title":"极差"}],"title":"对项目了解程度"},{"answer":"40","id":8,"list":[{"id":39,"seqId":1,"title":"否"},{"id":40,"seqId":2,"title":"是且之前是微整"},{"id":41,"seqId":3,"title":"是且之前是手术"}],"title":"是否复购客户"},{"answer":"43","id":9,"list":[{"id":42,"seqId":1,"title":"否"},{"id":43,"seqId":2,"title":"复购第二次"},{"id":44,"seqId":3,"title":"复购第三次"},{"id":45,"seqId":4,"title":"复购第四次及以上"}],"title":"复购次数"},{"answer":"46","id":10,"list":[{"id":46,"seqId":1,"title":"是"},{"id":47,"seqId":2,"title":"否"}],"title":"是否有信用卡"},{"answer":"49","id":11,"list":[{"id":48,"seqId":1,"title":"是"},{"id":49,"seqId":2,"title":"否"}],"title":"是否预警"}]},"taskType":"1","userBasicInfo":{"age":27,"blackBoxId":"B33145E4-969B-432A-9EE6-7E5BDC76CBB9","callHistoryJobId":"14e33d09-8265-467e-b0b7-4093aa31a7e0","company":"东方魅力","consumerCoefficient":"0.6376190476190476","creditCardNo":"6221550351882919","creditLimit":10000,"domain":"媒体/娱乐/体育","dueDate":"2024-01","educationDegree":"MIDDLE_SCHOOL","email":"396654970@qq.com","gender":"FEMALE","homeAddress":"浙江省嘉善县惠民街道大泖村河墩2号","houseCity":"125","houseProvince":"12","idCardAddress":"浙江省嘉善县惠民街道大泖村河墩2号","idCardPhotoBack":"https://api.xiaofen.net.cn//static/attachments/20175616/ad8f59b1-d54e-4609-944a-17175643fcf2_file.jpg","idCardPhotoFront":"https://api.xiaofen.net.cn//static/attachments/20175616/0902935a-efc7-4c20-b58d-7e9d0f843f9a_file.jpg","idCardPhotoHand":"https://api.xiaofen.net.cn//static/attachments/20175816/e127dbdf-5eab-47be-949d-50bb4a0c2ba5_file.jpg","idNo":"330421198909021820","idNoValidityDate":"2035-10-04","job":"","jobName":"","jobType":"服务类员工","loanAppNumber":0,"mobile":"13645836311","platform":"IOS","realName":"朱静","schoolName":"","userKey":778}},"sendTime":1492337882097,"sequenceId":0,"source":"YM","type":"AUDIT_REQUEST","uniqKey":"0214923366828369045111"}
    """
    ###No projectNum
    # body="""
    # {"data":{"additionalMaterialList":[{"comment":"用户合照","name":"用户合照","path":"https://api.xiaofen.net.cn//static/attachments/20171516/ff2b57b6-89b9-4a9e-b3a3-15dffbca9a55_20170416181516.jpg"}],"applicationSn":"0214923366828369045111","applicationSource":"YM","contactList":[{"mobile":"13806709573","name":"若 依"},{"mobile":"13625733063","name":"朱忠良"}],"emergencyContactList":[{"mobile":"13625733063","name":"朱忠良","relation":"父母"}],"loanInfo":{"loanAmount":48000,"loanPurpose":"医美","orgAddress":"上海市黄浦区瑞金南路341号西北室","orgCode":"YMSHA0038","orgCoefficient":"0.9","orgName":"上海宏津企业管理有限公司锦坤门诊部","orgType":"--","product":"脂肪填充脂肪隆胸","projTotalAmount":45000,"projectDetails":[{"projName":"脂肪填充脂肪隆胸","projPrice":45000}]},"positionList":[{"createTime":"1492337302000","eventType":"LOGIN","ipAddress":"223.104.5.230, 223.111.213.20","lat":31.19952597141875,"lng":121.4648794575539},{"createTime":"1492336460000","eventType":"REGISTER","ipAddress":"223.104.5.230, 223.111.213.19","lat":31.199526,"lng":121.464879}],"questionnaire":{"orderSn":"021492336682836904","questions":[{"answer":"2","id":1,"list":[{"id":1,"seqId":1,"title":"是"},{"id":2,"seqId":2,"title":"否"}],"title":"是否渠道来客"},{"answer":"3","id":2,"list":[{"id":3,"seqId":1,"title":"公关"},{"id":4,"seqId":2,"title":"主播"},{"id":5,"seqId":3,"title":"网红"},{"id":6,"seqId":4,"title":"其他自由职业"},{"id":7,"seqId":5,"title":"服务业"},{"id":8,"seqId":6,"title":"媒体体育娱乐"},{"id":9,"seqId":7,"title":"学生"},{"id":10,"seqId":8,"title":"家庭主妇（一般）"},{"id":11,"seqId":9,"title":"家庭主妇（富裕）"},{"id":12,"seqId":10,"title":"其他"}],"title":"职业范畴"},{"answer":"16","id":3,"list":[{"id":13,"seqId":1,"title":"校园"},{"id":14,"seqId":2,"title":"网红直播"},{"id":15,"seqId":3,"title":"美容院"},{"id":16,"seqId":4,"title":"夜店"},{"id":17,"seqId":5,"title":"模特经纪"},{"id":18,"seqId":6,"title":"微整工作室"}],"title":"渠道来源"},{"answer":"20","id":4,"list":[{"id":19,"seqId":1,"title":"否"},{"id":20,"seqId":2,"title":"是且另1家"},{"id":21,"seqId":3,"title":"是且另2家"},{"id":22,"seqId":4,"title":"是且另3家及以上"}],"title":"是否申请了别家"},{"answer":"23","id":5,"list":[{"id":23,"seqId":1,"title":"否"},{"id":24,"seqId":2,"title":"是且低于10000"},{"id":25,"seqId":3,"title":"是且低于20000"},{"id":26,"seqId":4,"title":"是且低于30000"},{"id":27,"seqId":5,"title":"是且低于50000"},{"id":28,"seqId":6,"title":"是且高于50000"}],"title":"么么贷通过情况"},{"answer":"29","id":6,"list":[{"id":29,"seqId":1,"title":"优秀"},{"id":30,"seqId":2,"title":"良好"},{"id":31,"seqId":3,"title":"一般"},{"id":32,"seqId":4,"title":"较差"},{"id":33,"seqId":5,"title":"极差"}],"title":"客户基本情况"},{"answer":"34","id":7,"list":[{"id":34,"seqId":1,"title":"优秀"},{"id":35,"seqId":2,"title":"良好"},{"id":36,"seqId":3,"title":"一般"},{"id":37,"seqId":4,"title":"较差"},{"id":38,"seqId":5,"title":"极差"}],"title":"对项目了解程度"},{"answer":"40","id":8,"list":[{"id":39,"seqId":1,"title":"否"},{"id":40,"seqId":2,"title":"是且之前是微整"},{"id":41,"seqId":3,"title":"是且之前是手术"}],"title":"是否复购客户"},{"answer":"43","id":9,"list":[{"id":42,"seqId":1,"title":"否"},{"id":43,"seqId":2,"title":"复购第二次"},{"id":44,"seqId":3,"title":"复购第三次"},{"id":45,"seqId":4,"title":"复购第四次及以上"}],"title":"复购次数"},{"answer":"46","id":10,"list":[{"id":46,"seqId":1,"title":"是"},{"id":47,"seqId":2,"title":"否"}],"title":"是否有信用卡"},{"answer":"49","id":11,"list":[{"id":48,"seqId":1,"title":"是"},{"id":49,"seqId":2,"title":"否"}],"title":"是否预警"}]},"taskType":"1","userBasicInfo":{"age":27,"blackBoxId":"B33145E4-969B-432A-9EE6-7E5BDC76CBB9","callHistoryJobId":"14e33d09-8265-467e-b0b7-4093aa31a7e0","company":"东方魅力","consumerCoefficient":"0.6376190476190476","creditCardNo":"6221550351882919","creditLimit":10000,"domain":"媒体/娱乐/体育","dueDate":"2024-01","educationDegree":"MIDDLE_SCHOOL","email":"396654970@qq.com","gender":"FEMALE","homeAddress":"浙江省嘉善县惠民街道大泖村河墩2号","houseCity":"125","houseProvince":"12","idCardAddress":"浙江省嘉善县惠民街道大泖村河墩2号","idCardPhotoBack":"https://api.xiaofen.net.cn//static/attachments/20175616/ad8f59b1-d54e-4609-944a-17175643fcf2_file.jpg","idCardPhotoFront":"https://api.xiaofen.net.cn//static/attachments/20175616/0902935a-efc7-4c20-b58d-7e9d0f843f9a_file.jpg","idCardPhotoHand":"https://api.xiaofen.net.cn//static/attachments/20175816/e127dbdf-5eab-47be-949d-50bb4a0c2ba5_file.jpg","idNo":"330421198909021820","idNoValidityDate":"2035-10-04","job":"","jobName":"","jobType":"服务类员工","loanAppNumber":0,"mobile":"13645836311","platform":"IOS","realName":"朱静","schoolName":"","userKey":778}},"sendTime":1492337882097,"sequenceId":0,"source":"YM","type":"AUDIT_REQUEST","uniqKey":"0214923366828369045111"}
    # """

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
    # realName = '林朝玉'
    # idNo = '512501196512305186'
    realName = '马克龙'
    idNo = '110101198606250113'
    # realName = CharacterUtil.createName()
    # idNo = IdNoUtil.create_id_no()
    uniqKey = NumberUtil.timestamp1000()
    # taskType = sys.argv[1]
    # taskType = 1
    taskType = NumberUtil.randomNumber(10, 20)
    userKey = NumberUtil.random1000();
    print "idNo="+idNo
    send(idNo, taskType, uniqKey, realName, userKey)