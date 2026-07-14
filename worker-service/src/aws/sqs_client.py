import boto3
from config.settings import settings


class SQSClient:
    def __init__(self):
        self.client = boto3.client(
            service_name="sqs",
            endpoint_url=settings.AWS_ENDPOINT,
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

    def receive_message(self):
        queue_url = self.get_queue_url()

        response = self.client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=5,
        )

        return response

    def list_queues(self):
        return self.client.list_queues()
    
    def delete_message(self, receipt_handle):
        queue_url = self.get_queue_url()

        self.client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle,
    )
    def get_queue_url(self):
        response = self.client.get_queue_url(
            QueueName=settings.QUEUE_NAME
        )
        return response["QueueUrl"]

    def send_message(self, message: str):
        queue_url = self.get_queue_url()

        response = self.client.send_message(
            QueueUrl=queue_url,
            MessageBody=message,
        )

        return response


# Create a singleton instance
sqs_client = SQSClient()