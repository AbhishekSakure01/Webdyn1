import json

from aws.sqs_client import sqs_client
from processing.processor import processor


def main():

    response = sqs_client.receive_message()

    messages = response.get("Messages", [])

    if not messages:
        print("📭 No messages")
        return

    message = messages[0]

    event = json.loads(message["Body"])

    processor.process(event)

    sqs_client.delete_message(message["ReceiptHandle"])

    print("\n✅ Message deleted")


if __name__ == "__main__":
    main()