import os
import pika
import time

from liblog import *

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', '5672'))

class RabbitMQConnection:
	def __init__(self, host=RABBITMQ_HOST, port=RABBITMQ_PORT):
		self.host = host
		self.port = port
		self.connection = None

	def __enter__(self):
		while True:
			try:
				self.connection = pika.BlockingConnection(
					pika.ConnectionParameters(host=self.host, port=self.port)
				)
				break
			except pika.exceptions.AMQPConnectionError as e:
				log_info(f"Connection failed, retrying in 5 seconds: {e}")
				time.sleep(5)

		return self.connection

	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.connection and not self.connection.is_closed:
			self.connection.close()

class RabbitMQMessagingConsumer:
	def __init__(self, queue_name):
		self.queue_name = queue_name

	def declare_queue(self, channel):
		channel.queue_declare(queue=self.queue_name)

	def consume_messages(self, callback):
		with RabbitMQConnection() as connection:
			channel = connection.channel()
			self.declare_queue(channel)
			channel.basic_qos(prefetch_count=1)
			channel.basic_consume(queue=self.queue_name, on_message_callback=callback)
			channel.start_consuming()

class RabbitMQMessagingSender:
	def __init__(self, queue_name):
		self.queue_name = queue_name

	def declare_queue(self, channel):
		channel.queue_declare(queue=self.queue_name)

	def send_message(self, message):
		with RabbitMQConnection() as connection:
			channel = connection.channel()
			self.declare_queue(channel)
			channel.basic_publish(
				exchange='',
				routing_key=self.queue_name,
				body=message,
				properties=pika.BasicProperties(
					delivery_mode=2,  # make message persistent
				)
			)

def rabbitmq_new_connection():
# {
	rbc = RabbitMQConnection()
	return rbc
# }

def rabbitmq_new_consumer(queue_name):
# {
	consumer = RabbitMQMessagingConsumer(queue_name)
	return consumer
# }

def rabbitmq_new_sender(queue_name):
# {
	sender = RabbitMQMessagingSender(queue_name)
	return sender
# }