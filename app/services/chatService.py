from app.services.RetrievalService import RetriverService
from app.services.prompt_builder import PromptBuilder
from app.llm.llm_service import LLMService

class ChatService:

    def __init__(
        self,
        retrieval_service: RetriverService,
        prompt_builder: PromptBuilder,
        llm_service: LLMService,
    ):
        self._retrieval_service = retrieval_service
        self._prompt_builder = prompt_builder
        self._llm_service = llm_service

    def chat(
        self,
        question: str,
        document_id: str,
    ) -> str:

        results = self._retrieval_service.retrieve(question,document_id=document_id)

        prompt = self._prompt_builder.build_prompt(
            question,
            results,
        )

        answer = self._llm_service.generate(prompt)

        return answer.text