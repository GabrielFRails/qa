# 
# Copyright (c) Gabriel Freitas: gabriel.estudy.reis@gmail.com
# Wrapper for rabbitmq and pika
#

import pika
import json
import time
import datetime

def send_message(message: str, queue_name: str):
# {
	connection = get_pika_conection()
	channel = connection.channel()
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

def convert_ts_to_date(timestamp):
    # Convert timestamp to datetime object
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    
    # Format datetime object as HH:mm:ss
    formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
    
    return formatted_time

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
