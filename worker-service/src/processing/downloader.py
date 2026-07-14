import os

from aws.s3_client import s3_client


class Downloader:

    DOWNLOAD_DIR = "sample-data/downloads"

    def download(self, bucket, key):

        os.makedirs(self.DOWNLOAD_DIR, exist_ok=True)

        filename = os.path.basename(key)

        destination = os.path.join(
            self.DOWNLOAD_DIR,
            filename
        )

        s3_client.download_file(
            bucket=bucket,
            key=key,
            download_path=destination
        )

        return destination


downloader = Downloader()