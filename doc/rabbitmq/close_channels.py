import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

open_channels = connection._channels.values()

for ch in open_channels:
	ch.close()

connection.close()
