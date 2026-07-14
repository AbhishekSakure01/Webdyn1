import boto3
from config.settings import settings


class S3Client:
    def __init__(self):
        self.client = boto3.client(
            service_name="s3",
            endpoint_url=settings.AWS_ENDPOINT,
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

    def upload_file(self, file_path, bucket, key):
        self.client.upload_file(
            Filename=file_path,
            Bucket=bucket,
            Key=key,
        )

    def download_file(self, bucket, key, download_path):
        self.client.download_file(
            Bucket=bucket,
            Key=key,
            Filename=download_path,
        )


s3_client = S3Client()