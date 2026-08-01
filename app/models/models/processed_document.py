from datetime import datetime
from pydantic import BaseModel

class ProcessedDocument(BaseModel):
  document_id:str
  text:str
  word_count:int
  processed_at:datetime
  page_count:int

  