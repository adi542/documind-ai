from pathlib import Path
import json
from app.models.models.document import Document,DocumentStatus
from app.core.exceptions import RepositoryError

class DocumentRepository:

    def __init__(
        self,
        data_file: str = "data/document.json"
    ):

        self.data_file = Path(data_file)

        self.data_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self.data_file.exists():
            self.data_file.write_text("[]")

    def save(self,document:Document)->None:
        try:
          with self.data_file.open("r",encoding="utf-8") as f:
            documents = json.load(f)
          documents.append(document.model_dump(mode="json"))

          with self.data_file.open("w",encoding="utf-8") as f:
            json.dump(documents,f,indent=4)
        except (OSError,json.JSONDecodeError) as e:
            raise RepositoryError(
                f"file metadata cannot be saved in repositiary {document.original_filename}"
            ) from e


    def get_by_id(self, document_id: str) -> Document | None:
       print(f"Searching for: {repr(document_id)}")

       try:
          with self.data_file.open("r", encoding="utf-8") as f:
            python_arr = json.load(f)

          for i in python_arr:
            print(f"Stored id: {repr(i['id'])}")

            if i["id"] == document_id:
                print("MATCH FOUND")
                return Document.model_validate(i)

          print("NO MATCH FOUND")
          return None

       except (OSError, json.JSONDecodeError) as e:
        raise RepositoryError(
            f"file id {document_id} cannot be fetched: {e}"
        ) from e
    
    
    def update(self,Doc:Document)->None:
        found = False
        try:
          with self.data_file.open("r",encoding="utf-8") as f:
            documents = json.load(f)
          Docu = Doc.model_dump(mode="json")
          for i,document in enumerate(documents):
            if document["id"] == Doc.id:
                documents[i] = Docu;
                found = True
                break;

          if not found:
             raise RepositoryError(...)
       
          with self.data_file.open("w",encoding="utf-8") as f:
            json.dump(documents,f,indent=4)
        
        except (OSError,json.JSONDecodeError) as e:
           raise RepositoryError(
              f"file cannot be updated {Doc.original_filename}:{e}"
           ) from e
    