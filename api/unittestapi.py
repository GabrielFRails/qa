from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse

import pika, aio_pika

import time

app = FastAPI()

@app.get("/")
def read_root():
	return {"Hello": "World"}

async def unittest_feed_event_generator(request: Request):
# {
	connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
	channel = await connection.channel()
	queue = await channel.declare_queue("unittest")

	try:
		async with queue.iterator() as queue_iter:
			async for message in queue_iter:
				async with message.process():
					# Yield the message payload as SSE event
					yield {"data": message.body.decode()}
	finally:
		# Cleanup: Close the channel and connection
		await channel.close()
		await connection.close()
# }

@app.get("/feed")
async def unittest_feed(request: Request):
	event_generator = unittest_feed_event_generator(request)
	return EventSourceResponse(event_generator)