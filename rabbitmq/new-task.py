# #!/usr/bin/env python
# import os
# import sys
#
# import pika
#
#
# def main():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
#     channel = connection.channel()
#
#     # channel.queue_declare(queue='hello')
#     channel.queue_declare(queue="task_queue", durable=True)
#
#     message = " ".join(sys.argv[1:]) or "Hello World!"
#     # channel.basic_publish(exchange='',
#     #                       routing_key='hello',
#     #                       body=message)
#     channel.basic_publish(
#         exchange="",
#         routing_key="task_queue",
#         body=message,
#         properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE),
#     )
#
#     print(" [x] Sent %r" % message)
#
#     # channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
#     # print(" [x] Sent 'Hello World!'")
#     connection.close()
#
#
# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("Interrupted")
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)
