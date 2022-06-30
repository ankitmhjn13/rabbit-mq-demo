import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = connection.channel()
channel.queue_declare(queue="work_queue_demo", durable=True)

message = sys.argv[1] if len(sys.argv) > 1 else "dummy mesage"
channel.basic_publish(exchange="", routing_key="work_queue_demo", body=message, properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

connection.close()