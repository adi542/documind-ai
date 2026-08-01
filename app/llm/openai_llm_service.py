from openai import OpenAI
from app.models.models.llm_response import LLMResponse
from app.llm.llm_service import LLMService

class OpenAILLMService(LLMService):
  def __init__(self,client:OpenAI,model:str):
    self._client = client
    self._model = model
  def generate(self, prompt:str)->str:
    response = self._client.responses.create(
      model=self._model,
      input=prompt,
    )
    return LLMResponse(
      text=response.output_text
    )