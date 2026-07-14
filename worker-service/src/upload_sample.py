from aws.s3_client import s3_client

BUCKET = "webdyn-data"

KEY = "landing/device001/DATA/sample.csv.gz"

FILE_PATH = "sample-data/input/sample.csv.gz"

print("Uploading file...")

s3_client.upload_file(
    file_path=FILE_PATH,
    bucket=BUCKET,
    key=KEY,
)

print("✅ Upload completed successfully!")