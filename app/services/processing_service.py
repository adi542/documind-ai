from app.repositories.document_repo import DocumentRepository
from app.services.document_processor import DocumentProcessor
from app.models.models.processed_document import ProcessedDocument
from app.core.exceptions import DocumentNotFound
from app.core.exceptions import DocumentAlreadyProcessed
from app.models.models.document import DocumentStatus

class ProcessingService:
  def __init__(self,repository:DocumentRepository,processor:DocumentProcessor):
    self._repository = repository
    self._processor = processor

  def process_document(
      self,document_id:str,
  )->ProcessedDocument:
    print(f"Received document_id: {repr(document_id)}")
    document = self._repository.get_by_id(document_id)
    print(f"Document returned: {document}")
    if document is None:
      raise DocumentNotFound
    if document.status == DocumentStatus.PROCESSED:
      raise DocumentAlreadyProcessed
    document.status = DocumentStatus.PROCESSING
    self._repository.update(document)
    processed = self._processor.process(document)
    document.pages = processed.page_count;
    
    document.status = DocumentStatus.PROCESSED
    self._repository.update(document)
    
    return processed
    