import pika
import traceback


def callback(channel, method, properties, body):
    print("=========================")
    print("message is: %s" % body)
    print("=========================")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    
    results = channel.queue_declare(queue="", exclusive=True)
    queue_name = results.method.queue
    
    # binding the queue to exchange
    channel.queue_bind(exchange="logs", queue=queue_name)
    
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except Exception as exp:
        print("exception : %s raised" % str(exp))
        traceback.print_exc()
        exit()