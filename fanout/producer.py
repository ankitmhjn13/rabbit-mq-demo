import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# creating a new exchange of type fanout
channel.exchange_declare(exchange="logs", exchange_type="fanout")

message = sys.argv[1] if len(sys.argv) > 1 else "No Message"
print(message)

# we are publishing the message to exchange not to any queue
channel.basic_publish(exchange="logs", routing_key="", body=message)

connection.close()