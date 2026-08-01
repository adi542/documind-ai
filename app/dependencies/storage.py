from app.services.storage_service import StorageService
from app.services.document_processor import DocumentProcessor

_storage_service = StorageService()

_document_processor = DocumentProcessor(
    _storage_service
)


def get_storage_service() -> StorageService:
    return _storage_service


def get_document_processor() -> DocumentProcessor:
    return _document_processor