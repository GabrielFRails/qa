#!/usr/bin/env python
import pika, sys, os, json, subprocess

def main():
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	channel.queue_declare(queue='endpoint_tests')

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

	channel.basic_consume(queue='endpoint_tests', on_message_callback=callback, auto_ack=True)

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)