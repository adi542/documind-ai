from app.dependencies.repository import get_document_repository
from app.dependencies.storage import (
    get_storage_service,
    get_document_processor
)
from app.dependencies.vector_store import get_vector_store

from app.services.upload_service import UploadService
from app.services.processing_service import ProcessingService
from app.services.chunking_service import ChunkingService
from app.services.EmbeddingService import EmbeddingService
from app.services.IndexingService import IndexingService
from app.services.RetrievalService import RetriverService
from openai import OpenAI
from app.core.config import settings
from app.llm.openai_llm_service import OpenAILLMService
from app.services.prompt_builder import PromptBuilder
from app.services.chatService import ChatService
from app.llm.llm_service import LLMService
from app.core.config import settings

# Repository
_document_repository = get_document_repository()

# Storage
_storage_service = get_storage_service()
_document_processor = get_document_processor()

# Vector Store
_vector_store = get_vector_store()

_upload_service = UploadService(
    storage_service=_storage_service,
    document_repository=_document_repository
)

_processing_service = ProcessingService(
    repository=_document_repository,
    processor=_document_processor
)

_chunking_service = ChunkingService()

_embedding_service = EmbeddingService(
    model_name=settings.EMBEDDING_MODEL
)

_indexing_service = IndexingService(
    document_repository=_document_repository,
    processing_service=_processing_service,
    chunking_service=_chunking_service,
    embedding_service=_embedding_service,
    vector_store=_vector_store
)
def get_upload_service() -> UploadService:
    return _upload_service


def get_processing_service() -> ProcessingService:
    return _processing_service


def get_indexing_service() -> IndexingService:
    return _indexing_service

_openai_client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

_llm_service = OpenAILLMService(
    client=_openai_client,
    model=settings.OPENAI_MODEL,
)

_retrieval_service =  RetriverService(
    embedding_service=_embedding_service,
    vectorStore=_vector_store
)

_prompt_builder = PromptBuilder()

_chat_service = ChatService(
    retrieval_service=_retrieval_service,
    prompt_builder=_prompt_builder,
    llm_service=_llm_service,
)

def get_chat_service() -> ChatService:
    return _chat_service


def get_llm_service() -> LLMService:
    return _llm_service


def get_retrieval_service() -> RetriverService:
    return _retrieval_service