from typing import List

from .QuoteModel import QuoteModel
from .Ingestor_Interface import IngestorInterface


class Text_Ingestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest specified file')

        author = []
        #doc = txt.Document(path)

        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                if line != "":
                    text = line.strip().split(' - ')
                    final_author = QuoteModel(text[0],text[1])
                    author.append(final_author)

        #f.close()

        return author