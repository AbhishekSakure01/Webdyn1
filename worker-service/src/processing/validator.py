class Validator:

    REQUIRED_COLUMNS = [
        "timestamp",
        "voltage",
        "current",
        "power",
    ]

    def validate(self, records):

        if not records:
            raise ValueError("CSV contains no records.")

        for index, record in enumerate(records, start=1):

            for column in self.REQUIRED_COLUMNS:

                if column not in record:
                    raise ValueError(
                        f"Missing column '{column}' in record {index}"
                    )

                if record[column] is None or record[column] == "":
                    raise ValueError(
                        f"Empty value for '{column}' in record {index}"
                    )

        return True


validator = Validator()