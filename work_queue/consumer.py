import pika
import traceback
import time

def callback(channel, method, properties, body):
    print("=========================")
    print(f"body: {body}")
    print("=========================")
    print("\n\n\n\n")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="work_queue_demo", durable=True)
    channel.basic_qos(prefetch_count=2)
    channel.basic_consume(queue="work_queue_demo", on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except Exception as exp:
        print(f"{exp} raised.")
        traceback.print_exc()
        exit()