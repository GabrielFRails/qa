#!/usr/bin/env python
import pika, sys, os, json, subprocess, time

def main():
	rabbitmq_host = os.getenv('RABBITMQ_HOST')
	rabbitmq_port = int(os.getenv('RABBITMQ_PORT'))
	queue_name = 'test_queue'
	#connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
	#channel = connection.channel()
	#channel.queue_declare(queue=queue_name)

	while True:
		try:
			connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port))
			channel = connection.channel()
			channel.queue_declare(queue=queue_name)
			print(f"Connection and channel ok.")
			break
		except pika.exceptions.AMQPConnectionError as e:
			print(f"Connection failed, retrying in 5 seconds: {e}")
			time.sleep(5)

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

	channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

	print(' [*] Waiting for messages.')
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