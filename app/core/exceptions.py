class DocuMindError(Exception):
    """Base exception for the entire application."""
    pass


class UnsupportedFileType(DocuMindError):
    """Raised when an unsupported file type is uploaded."""
    pass


class StorageError(DocuMindError):
    """Raised when storing or deleting a file fails."""
    pass


class RepositoryError(DocuMindError):
    """Raised when reading or writing document metadata fails."""
    pass


class DocumentProcessingError(DocuMindError):
    """Raised when document processing fails."""
    pass


class DocumentNotFound(DocuMindError):
    """Raised when a document cannot be found."""
    pass


class DocumentAlreadyProcessed(DocuMindError):
    """Raised when a processed document is processed again."""
    pass