from dataclasses import dataclass


@dataclass
class S3Event:
    device_id: str
    bucket: str
    key: str