# -*- coding:utf-8 -*-
# !/usr/bin/env python

from com.abin.lee.thread.config import RabbitmqConfig

import pika

# ########################## 消费者 ##########################
credentials = pika.PlainCredentials(RabbitmqConfig.RabbitmqEnum.RABBITMQ_USER, RabbitmqConfig.RabbitmqEnum.RABBITMQ_PWD)
# 连接到rabbitmq服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(RabbitmqConfig.RabbitmqEnum.RABBITMQ_HOST,RabbitmqConfig.RabbitmqEnum.RABBITMQ_PORT,RabbitmqConfig.RabbitmqEnum.RABBITMQ_VIRTUAL_HOST,credentials))
channel = connection.channel()

# 声明消息队列，消息将在这个队列中进行传递。如果队列不存在，则创建
channel.queue_declare(queue=RabbitmqConfig.RabbitmqEnum.RABBITMQ_QUEUE)


# 定义一个回调函数来处理，这边的回调函数就是将信息打印出来。
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print("body=" % body)


# 告诉rabbitmq使用callback来接收信息
channel.basic_consume(callback,
                      queue=RabbitmqConfig.RabbitmqEnum.RABBITMQ_QUEUE,
                      no_ack=True)
 # no_ack=True表示在回调函数中不需要发送确认标识

print(' [*] Waiting for messages. To exit press CTRL+C')

# 开始接收信息，并进入阻塞状态，队列里有信息才会调用callback进行处理。按ctrl+c退出。
channel.start_consuming()