import json
from aws.sqs_client import sqs_client

event = {
    "device_id": "device001",
    "bucket": "webdyn-data",
    "key": "landing/device001/DATA/sample.csv.gz"
}

response = sqs_client.send_message(json.dumps(event))

print("✅ Event Sent")
print("Message ID:", response["MessageId"])