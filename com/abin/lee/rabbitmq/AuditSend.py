# -*- coding:utf-8 -*-
#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest', 'guest')
#这里可以连接远程IP，请记得打开远程端口
parameters = pika.ConnectionParameters('172.16.2.145',15671,'/',credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# channel.queue_declare(queue='audit.request.queue')
uniqKey = "1000000000080"
taskType = sys.argv[1]
# taskType = "2"
body = "{\"sendTime\":1482116888000,\"uniqKey\":"+uniqKey+",\"source\":\"RRD\",\"type\":\"AUDIT_REQUEST\",\"sequenceId\":0,\"data\":{\"applicationSn\":"+uniqKey+",\"applicationSource\":\"RRD\",\"createTime\":1482116888000,\"taskType\":"+taskType+",\"description\":\"用户首次进件啊啊啊\",\"loanInfo\":{\"productCode\":\"000001\",\"product\":\"玻尿酸500ml\",\"organizationCode\":\"10000\",\"organization\":\"xx整形\",\"organizationLevel\":\"5\",\"orgType\":\"机构类型类型类型\",\"orgLng\":123.45,\"orgLat\":67.89,\"productPrice\":5000.00,\"loanPhase\":6,\"loanAmount\":4000.00,\"loanPurpose\":\"美颜没演美艳\"},\"userBasicInfo\":{\"userKey\":\"fefigfefbvkdeifgi\",\"idNo\":\" 431381198109106573\",\"realName\":\"罗淳雅\",\"gender\":\"MALE\",\"idNoValidityDate\":\"2020-12-31\",\"mobile\":\"15088741234\",\"reserveMobile\":\"15088741234\",\"email\":\"xx@xx.com\",\"origin\":\"**\",\"loanAppNumber\":7,\"homeAddress\":\"**\",\"homeCity\":\"**\",\"homeDistrict\":\"**\",\"homeProvince\":\"**\",\"houseAddress\":\"**\",\"houseCity\":\"**\",\"houseDistrict\":\"**\",\"houseProvince\":\"**\",\"idCardAddress\":\"xxxx\",\"cityLocationCity\":\"**\",\"cityLocationProvince\":\"**\",\"blackBoxId\":\"**\",\"platform\":\"**\",\"cardNo\":\"622123412341234\",\"educationDegree\":\"COLLEGE\",\"graduateDate\":\"2002-12-31\",\"creditCardNo\":\"600xxxxxx\",\"creditLimit\":20000.00,\"dueDate\":\"2020-12-12\",\"job\":\"xx\",\"jobName\":\"xx\",\"domain\":\"xxx\",\"jobType\":\"xx\",\"company\":\"xxxx\",\"companyPhone\":\"xxxx\",\"idCardPhotoFront\":\"http://dev.zs.heika.com/res/restaurant/b40ad163-8351-4a31-a5e1-225d31db47c2.jpg\",\"idCardPhotoBack\":\"http://dev.zs.heika.com/res/restaurant/b40ad163-8351-4a31-a5e1-225d31db47c2.jpg\",\"idCardPhotoHand\":\"http://dev.zs.heika.com/res/restaurant/b40ad163-8351-4a31-a5e1-225d31db47c2.jpg\"},\"emergencyContactList\":[{\"mobile\":\"15011212120\",\"name\":\"季长业\",\"relation\":\"弟弟\"},{\"mobile\":\"15011212121\",\"name\":\"羽然\",\"relation\":\"朋友\"}],\"contactList\":[{\"mobile\":\"15088741234\",\"name\":\"大大\"},{\"mobile\":\"15088741234\",\"name\":\"大大大\"},{\"mobile\":\"15088741234\",\"name\":\"大大大大\"}],\"positionList\":[{\"createTime\":1482116888000,\"eventType\":\"LOGIN\",\"geocodePosition\":\"北京市海淀区清华科技园\",\"ipAddress\":\"222.222.222.222\",\"ipPosition\":\"北京市海淀区\",\"lat\":36.45,\"lng\":123.45}],\"additionalMaterialList\":[{\"name\":\"身份证照片\",\"path\":\"http://dev.zs.heika.com/res/restaurant/b40ad163-8351-4a31-a5e1-225d31db47c2.jpg\",\"comment\":\"长相很有特色\"},{\"name\":\"合同\",\"path\":\"http://dev.zs.heika.com/res/restaurant/b40ad163-8351-4a31-a5e1-225d31db47c2.jpg\",\"comment\":\"呵呵呵呵同\"}]}}"
channel.basic_publish(exchange='',
                      routing_key='audit.request.queue',
                      body=body)
print " [x] Sent %s" %body
connection.close()