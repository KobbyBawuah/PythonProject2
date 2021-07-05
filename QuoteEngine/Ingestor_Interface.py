from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface:
	allowed_extension = []

	@classmethod
	@abstractmethod
	def parse(cls, path:str) -> List[QuoteModel]:
		pass

	@classmethod
	def can_ingest(cls, path):
		print("here")
		print(path)
		ext = path.split('.')[-1]
		print(ext)
		print(cls.allowed_extension)
		print(ext in cls.allowed_extension)
		return ext in cls.allowed_extension