from app.services.storage_service import StorageService
from app.models.models.document import Document,DocumentStatus,DocumentType
from app.models.models.processed_document import ProcessedDocument
from app.core.exceptions import DocumentProcessingError
import fitz
from pathlib import Path
from datetime import datetime
import re


class DocumentProcessor:

    def __init__(
        self,
        storage: StorageService
    ):
        self._storage = storage
        self.page_count = 0;

    def process(
       self,
      document: Document
       ) -> ProcessedDocument:
      path = self._storage.get_path(document.stored_filename);
      text = self._extract_text(path)
      clean_text = self._clean_text(text)
      proccesed_document = self._build_processed_document(
         clean_text,document,self.page_count
      )
      return proccesed_document
    
    def _extract_text(self,path:Path):
       pages = [];
       try:
        with fitz.open(path) as pdf:
          for page in pdf:
             pages.append(page.get_text())
        self.page_count = len(pages)
        return "\n".join(pages)
       except Exception as e:
          raise DocumentProcessingError(
             f"File cannot be open:{e}"
          ) from e
         
    def _clean_text(self, text: str) -> str:

      text = text.strip()

      text = text.replace("\t", " ")

      text = re.sub(r"[ ]+", " ", text)

      text = re.sub(r"\n{3,}", "\n\n", text)

      return text
    
    def _build_processed_document(self,text:str,document:Document,pages_count:int)->ProcessedDocument:
       return ProcessedDocument(
          document_id=document.id,
          text = text,
          word_count=len(text.split()),
          processed_at=datetime.now(),
          page_count=pages_count
       )
       