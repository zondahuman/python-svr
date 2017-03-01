
import pika

connection = pika.BlockingConnection('172.16.2.145',15671)
channel = connection.channel()
channel.basic_publish(exchange='example',
                      routing_key='test',
                      body='Test Message')
connection.close()