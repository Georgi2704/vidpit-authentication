# #!/usr/bin/env python
# import pika
#
# from server.api.deps import get_current_user
#
#
# def start_listening():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
#
#     channel = connection.channel()
#
#     channel.queue_declare(queue="vidpit_auth")
#
#     channel.basic_qos(prefetch_count=1)
#     channel.basic_consume(queue="vidpit_auth", on_message_callback=on_request)
#
#     print(" [x] Awaiting RPC requests")
#     channel.start_consuming()
#
#
# def on_request(ch, method, props, body):
#     token = str(body.decode("utf-8"))
#     # token = str(body)
#
#     print(" [.] token(%s)" % token)
#     response = None
#     try:
#         response = get_current_user(token)
#     except Exception as e:
#         response = str(e.__dict__)
#
#     print(" [.] user(%s)" % response)
#
#     ch.basic_publish(
#         exchange="",
#         routing_key=props.reply_to,
#         properties=pika.BasicProperties(correlation_id=props.correlation_id),
#         body=str(response),
#     )
#     ch.basic_ack(delivery_tag=method.delivery_tag)
