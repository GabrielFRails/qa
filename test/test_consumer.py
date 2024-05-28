#!/usr/bin/env python
#import pika
#import time

import sys
import os
import json
import subprocess

from librabbitmq import *
from liblog import *

def main():
	queue_name = 'test_queue'
	local_consumer = rabbitmq_new_consumer(queue_name)

	def callback(ch, method, properties, body):
		log_info(f" [x] Received {body} - {type(body)}")
		try:
			msg_dict = json.loads(body)
			command = msg_dict['command']
			log_info(command)
			if command == "runtests":
				subprocess.run(['make', 'runtests'])
		except:
			log_info(f"message can not be converted to dict: {body}")

	log_info(' [*] Waiting for messages.')
	local_consumer.consume_messages(callback)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		log_info('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)