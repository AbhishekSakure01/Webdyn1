import os


class MetadataBuilder:

    def build(self, event, records):

        return {
            "device_id": event["device_id"],
            "filename": os.path.basename(event["key"]),
            "record_count": len(records),
            "start_time": records[0]["timestamp"],
            "end_time": records[-1]["timestamp"],
        }


metadata_builder = MetadataBuilder()