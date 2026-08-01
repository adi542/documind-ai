from pydantic import BaseModel

class Chunk(BaseModel):
  id:str
  document_id:str
  chunk_index:int
  text:str
  word_count:int
  start_offset:int
  end_offset:int