#!/usr/bin/env python
import os
import sys

import pika


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    # # Declare a queue with a random name
    # result = channel.queue_declare(queue='', exclusive=True)
    #
    # # Тell the exchange to send messages to our queue
    # channel.queue_bind(exchange='logs',
    #                    queue=result.method.queue)

    message = ' '.join(sys.argv[1:]) or "Hello World!"

    channel.basic_publish(exchange='logs', routing_key='', body=message)

    print(" [x] Sent %r" % message)
    connection.close()

    # channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    # print(" [x] Sent 'Hello World!'")
    # connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)