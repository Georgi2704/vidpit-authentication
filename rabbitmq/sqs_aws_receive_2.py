import json

import boto3
import os
from dotenv import load_dotenv

from server.api.deps import check_current_active_superuser, get_current_user


def to_dict(self):
    return json.loads(json.dumps(self, default=lambda o: o.__dict__))


def send_back_decoded(queue_id):
    # queue_jwt = "https://sqs.eu-central-1.amazonaws.com/302645174876/JwtTokens"
    print(queue_id)
    queue_url = f"https://sqs.eu-central-1.amazonaws.com/302645174876/{queue_id}"
    print(queue_url)
    type="decoded"

    # # Create SQS client
    # sqs = boto3.client(
    #     'sqs',
    #     aws_access_key_id=os.getenv("SQS_ACCESS_KEY_ID"),
    #     aws_secret_access_key=os.getenv("SQS_SECRET_ACCESS_KEY"),
    # )
    #
    #
    # # Receive message from SQS queue
    # response = sqs.receive_message(
    #     QueueUrl=queue_url,
    #     MaxNumberOfMessages=1,
    #     VisibilityTimeout=20,
    #     WaitTimeSeconds=20,
    # )
    # print(response)
    # message = response['Messages'][0]
    # receipt_handle = message['ReceiptHandle']
    # body = json.loads(message['Body'])
    # correlation_id = body['correlation_id']
    # jwt_token = body['jwt_token']
    # payload = {}
    # try:
    #     user = get_current_user(jwt_token)
    #     payload = {
    #         "type": f"{type}",
    #         "user": f"{vars(user)}"
    #     }
    # except:
    #     payload = {
    #         "correlation_id": f"{type}",
    #         "user": "403"
    #     }
    # # Delete received message from queue
    # sqs.delete_message(
    #     QueueUrl=queue_url,
    #     ReceiptHandle=receipt_handle
    # )
    # print('Received and deleted message: %s' % message)
    #
    # payload2 = json.dumps(payload)
    # sqs.send_message(
    #     QueueUrl=queue_url,
    #     MessageBody=payload2
    # )


if __name__ == '__main__':
    load_dotenv()
    send_back_decoded()
