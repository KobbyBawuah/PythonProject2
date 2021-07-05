from typing import List
import docx 

from .QuoteModel import QuoteModel
from .Ingestor_Interface import IngestorInterface


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest specified file')

        authordocx = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_dog = QuoteModel(parse[0], parse[1])
                authordocx.append(new_dog)

        return authordocx