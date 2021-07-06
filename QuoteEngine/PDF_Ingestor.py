from typing import List
import subprocess
import os
import random
import sys

from .QuoteModel import QuoteModel
from .Ingestor_Interface import IngestorInterface


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest specified file')

        tmp = "/output.txt"

        subprocess.run(["pdftotext.exe", "-layout",
                        "-nopgbrk", path, tmp])

        author_pdf = []

        with open(tmp) as file:
            lines = file.readlines()
            for line in lines:
                parse = line.split('-')
                last_pdf = QuoteModel(parse[0], int(parse[1]).strip('\n'))
                author_pdf.append(new_cat)

            file.close()

        return author_pdf
