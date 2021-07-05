from typing import List
import pandas

from .QuoteModel import QuoteModel
from .Ingestor_Interface import IngestorInterface

class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest specified file')
        try:
            author_csv = []
            df = pandas.read_csv(path, header=0)

            for index, row in df.iterrows():
                new_author = QuoteModel(row['body'], row['author'])
                author_csv.append(new_author)
        except Exception as e:
            raise Exception("CSV parsing issue occured.")    
        return author_csv