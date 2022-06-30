import pika
import traceback
import time

def callback(channel, method, properties, body):
    time.sleep(10)
    print("=========================")
    print(f"channel: {channel}")
    print(f"method: {method}")
    print(f"properties: {properties}")
    print(f"body: {body}")
    print("=========================")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="demo")
    # if the message is not acknowledged 
    # while consuming it will be kept in 
    # unacked state and will be read by 
    # the consumer is restarted again
    channel.basic_consume(queue="demo", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except Exception as exp:
        print(f"{exp} raised.")
        traceback.print_exc()
        exit()