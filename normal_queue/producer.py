import pika


connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
result = channel.queue_declare(queue="demo")


# to publish the message to queue with defualt exchange the routuing key name should be same as of queue name
channel.basic_publish(exchange="", routing_key="demo", body="hello world")

connection.close()