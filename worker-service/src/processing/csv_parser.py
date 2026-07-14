import csv


class CSVParser:

    def parse(self, csv_file):

        rows = []

        with open(csv_file, newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                rows.append({
                    "timestamp": row["timestamp"],
                    "voltage": float(row["voltage"]),
                    "current": float(row["current"]),
                    "power": float(row["power"]),
                })

        return rows


csv_parser = CSVParser()