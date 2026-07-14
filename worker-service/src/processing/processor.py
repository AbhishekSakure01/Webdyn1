from processing.downloader import downloader
from processing.decompressor import decompressor
from processing.csv_parser import csv_parser
from processing.validator import validator
from processing.metadata import metadata_builder


class WorkerProcessor:

    def process(self, event):

        downloaded_file = downloader.download(
            bucket=event["bucket"],
            key=event["key"],
        )

        print("\nDownloaded File:")
        print(downloaded_file)

        csv_file = decompressor.decompress(downloaded_file)

        print("\nCSV File:")
        print(csv_file)

        records = csv_parser.parse(csv_file)

        print(f"\nRecords Found: {len(records)}")

        validator.validate(records)

        metadata = metadata_builder.build(event, records)

        print("\nMetadata:")
        print(metadata)

        return metadata


processor = WorkerProcessor()