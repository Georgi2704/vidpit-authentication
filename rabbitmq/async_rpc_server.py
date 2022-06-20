import asyncio
import json
import logging

from aio_pika import Message, connect
from aio_pika.abc import AbstractIncomingMessage

from server.api.deps import check_current_active_superuser, get_current_active_superuser, get_current_user

# def fib(n: int) -> int:
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


async def start_listening() -> None:
    # Perform connection
    connection = await connect("amqp://guest:guest@localhost/")

    # Creating a channel
    channel = await connection.channel()
    exchange = channel.default_exchange

    # Declaring queue
    queue = await channel.declare_queue("rpc_queue")

    print(" [x] Awaiting RPC requests")

    # Start listening the queue with name 'hello'
    async with queue.iterator() as qiterator:
        message: AbstractIncomingMessage
        async for message in qiterator:
            try:
                async with message.process(requeue=False):
                    assert message.reply_to is not None
                    print("not decoded: " + str(message.body))
                    token = str(message.body.decode())
                    print("decoded: " + token)
                    response = None
                    try:
                        response = str(check_current_active_superuser(get_current_user(token))).encode()
                        print("to be sent: " + str(response))
                    except Exception as e:
                        response = str(e.__dict__).encode()
                        print("exception:" + str(response))

                    await exchange.publish(
                        Message(
                            body=response,
                            correlation_id=message.correlation_id,
                        ),
                        routing_key=message.reply_to,
                    )
                    print("Request complete")
            except Exception:
                logging.exception("Processing error for message %r", message)

if __name__ == "__main__":
    asyncio.run(start_listening())