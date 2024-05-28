#!/usr/bin/env python
#import pika
#import time

import sys
import os
import json
import subprocess

from librabbitmq import *

def main():
	queue_name = 'test_queue'
	local_consumer = rabbitmq_new_consumer(queue_name)

	def callback(ch, method, properties, body):
		print(f" [x] Received {body} - {type(body)}")
		try:
			msg_dict = json.loads(body)
			command = msg_dict['command']
			print(command)
			if command == "runtests":
				subprocess.run(['make', 'runtests'])
		except:
			print(f"message can not be converted to dict: {body}")

	print(' [*] Waiting for messages.')
	local_consumer.consume_messages(callback)

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)