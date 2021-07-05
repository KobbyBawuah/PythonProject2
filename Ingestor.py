from QuoteEngine.CSV_Ingestor import CSVIngestor
from QuoteEngine.Doc_Ingestor import DocxIngestor
from QuoteEngine.PDF_Ingestor import PDFIngestor
from QuoteEngine.Text_Ingestor import Text_Ingestor

from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.Ingestor_Interface import IngestorInterface

from typing import List

class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor, PDFIngestor, DocxIngestor, Text_Ingestor]

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            print(path)
            print(ingestor)
            if ingestor.can_ingest(path):
                print("yes")
                print(ingestor)
                print(path)
                return ingestor.parse(path)