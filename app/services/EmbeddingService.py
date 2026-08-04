# from sentence_transformers import SentenceTransformer
from openai import OpenAI
from app.models.models.chunk import Chunk
from app.models.models.embeddingclass import EmbeddedChunk
class EmbeddingService():
  def __init__(self,model_name:str,client:OpenAI):
    self._model_name = model_name
    self._client = client
    self._model = None
  

   
  def embed_chunks(self,chunks:list[Chunk]) ->list[EmbeddedChunk]:
    embeddings_chunk = []
    for chunk in chunks:
      embeddings = self._embed_chunk(chunk)
      embedded_chunk = self._build_embedded_chunk(
        chunk,embeddings
      )
      embeddings_chunk.append(embedded_chunk)
    return embeddings_chunk



  # def _embed_chunk(self,chunk:Chunk) ->list[float]:
  #   embeddings = self._get_model().encode(chunk.text,convert_to_numpy=True).tolist()
  #   return embeddings

  def _embed_chunk(
    self,
    chunk: Chunk,
) -> list[float]:

    response = self._client.embeddings.create(
        model=self._model_name,
        input=chunk.text,
    )

    return response.data[0].embedding
  

  def _build_embedded_chunk(self,chunck:Chunk,embedding:list[float])->EmbeddedChunk:
    return EmbeddedChunk(
      chunk=chunck,
      embeddings=embedding
    )

  # def embed_query(self,query:str)->list[float]:
  #   return self._get_model().encode(query,convert_to_numpy=True).tolist()

  def embed_query(
    self,
    query: str,
) -> list[float]:

    response = self._client.embeddings.create(
        model=self._model_name,
        input=query,
    )

    return response.data[0].embedding