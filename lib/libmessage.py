# 
# Copyright (c) Gabriel Freitas: gabriel.estudy.reis@gmail.com
# Wrapper for rabbitmq and pika
#

import pika
import json
import time
import datetime
import os

rabbitmq_host = os.getenv('RABBITMQ_HOST', 'localhost')
rabbitmq_port = int(os.getenv('RABBITMQ_PORT', '5672'))

def send_message(message: str, queue_name: str, channel):
# {
	channel.queue_declare(queue=queue_name)
	channel.basic_publish(exchange='', routing_key=queue_name, body=message)
# }

def generate_unittest_message(testid: str, test_status: str) -> str:
# {
	ts = time.time()
	message = {
		"testid_str": testid,
		"test_status": test_status,
		"ts": ts,
		"ts_str": convert_ts_to_date(ts)
	}

	msg_json = json.dumps(message)
	return msg_json
# }

def generate_command_message(command: str, origin: str) -> str:
# {
	ts = time.time()
	message = {
		"origin": origin,
		"command": command,
		"ts": ts,
		"ts_str": convert_ts_to_date(ts)
	}

	msg_json = json.dumps(message)
	return msg_json
# }

def convert_ts_to_date(timestamp):
	dt_object = datetime.datetime.fromtimestamp(timestamp)
	formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
	return formatted_time

__pika_connection = None
def get_pika_connection():
# {
	global __pika_connection
	if not __pika_connection:
		__pika_connection =  pika.BlockingConnection(
			pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))

	return __pika_connection
# }

__unittest_msg_channel = None
def get_msg_channel():
# {
	global __unittest_msg_channel
	if not __unittest_msg_channel:
		connection = get_pika_connection()
		__unittest_msg_channel = message_open_channel(connection)

	return __unittest_msg_channel
# }

def close_connection():
# {
	connection = get_pika_connection()
	connection.close()
# }

def message_open_connection():
# {
	pika_connection =  pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	return pika_connection
# }

def message_close_connection(connection):
# {
	connection.close()
# }

def message_open_channel(connection):
# {
	channel = connection.channel()
	return channel
# }

def message_close_channel(channel):
# {
	channel.close()
# }