#!/usr/bin/env python
import pika, time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(0, 11):
	channel.basic_publish(exchange='', routing_key='hello', body=f'Hello World! {i}')
	print(f" [x] Sent 'Hello World! {i}'")
	time.sleep(1)

connection.close()