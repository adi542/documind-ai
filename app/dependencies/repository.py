from app.repositories.document_repo import DocumentRepository

_document_repository = DocumentRepository()


def get_document_repository() -> DocumentRepository:
    return _document_repository