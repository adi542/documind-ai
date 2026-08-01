from pathlib import Path
from fastapi import UploadFile
from app.core.exceptions import StorageError
import shutil

class StorageService:
  def __init__(self,upload_dir:str = "uploads"):
    self.upload_dir = Path(upload_dir)
    self.upload_dir.mkdir(
      parents=True,
      exist_ok=True
    )
    
  def save(self,file:UploadFile,filename:str)->Path:
    destination = self.upload_dir/filename
    try:
      with destination.open("wb") as buffer:
       shutil.copyfileobj(
        file.file,
        buffer
      )
      return destination
    except OSError as e:
      raise StorageError(
        f"Failed to save file: {e}"
      ) from e

    
  
  def delete(self,path:Path):
    try:
      if path.exists():
       path.unlink()
    except OSError as e:
      raise StorageError(
        f"File cannot be deleted:{e}"
      ) from e

  def get_path(self,stored_filename:str)->Path:
      return self.upload_dir / stored_filename
    
