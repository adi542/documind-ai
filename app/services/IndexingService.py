from app.repositories.document_repo import DocumentRepository
from app.services.processing_service import ProcessingService
from app.services.chunking_service import ChunkingService
from app.services.EmbeddingService import EmbeddingService
from app.vectorStores.vector_store import VectorStore
from app.schemas.processing_response import ProcessingResponse


class IndexingService:

    def __init__(
        self,
        document_repository: DocumentRepository,
        processing_service: ProcessingService,
        chunking_service: ChunkingService,
        embedding_service: EmbeddingService,
        vector_store: VectorStore,
    ):
        self._document_repository = document_repository
        self._processing_service = processing_service
        self._chunking_service = chunking_service
        self._embedding_service = embedding_service
        self._vector_store = vector_store

    def index_document(self,document_id:str)->ProcessingResponse:
        processed_document = self._processing_service.process_document(document_id=document_id)
        chunks = self._chunking_service.chunk_document(processed_document)
        embedded_chunks = self._embedding_service.embed_chunks(chunks)
        self._vector_store.add(embedded_chunks)
        return processed_document
        
        