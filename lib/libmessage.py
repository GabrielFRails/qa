# 
# Copyright (c) Gabriel Freitas: gabriel.estudy.reis@gmail.com
# Wrapper for rabbitmq and pika
#

import pika

def send_message(message: str, queue_name: str):
# {
	connection = get_pika_conection()
	channel = connection.channel()
	channel.queue_declare(queue=queue_name)
	channel.basic_publish(exchange='', routing_key=queue_name, body=message)
# }

__pika_connection = None
def get_pika_conection():
# {
	global __pika_connection
	if not __pika_connection:
		__pika_connection =  pika.BlockingConnection(
			pika.ConnectionParameters(host='localhost'))

	return __pika_connection
# }

def close_connection():
# {
	connection = get_pika_conection()
	connection.close()
# }
