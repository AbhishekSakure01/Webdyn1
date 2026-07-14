import gzip
import shutil
import os


class Decompressor:

    def decompress(self, gz_file):

        csv_file = os.path.splitext(gz_file)[0]

        with gzip.open(gz_file, "rb") as f_in:
            with open(csv_file, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

        return csv_file


decompressor = Decompressor()