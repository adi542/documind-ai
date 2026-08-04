from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Depends
)

# from app.services.upload_service import UploadService
# from app.services.processing_service import ProcessingService
# from app.dependencies.services import (
#     get_chat_service,
# )
# from app.dependencies.services import (
#     get_upload_service,
#     get_processing_service
# )
from app.models.models.ChatRequest import ChatRequest
from app.schemas.upload_response import UploadResponse
from app.schemas.processing_response import ProcessingResponse

# from app.models.models.document import DocumentStatus

# from app.core.exceptions import (
#     UnsupportedFileType
# )
# from app.models.models.chatresponse import ChatResponse
# from app.services.chatService import ChatService

# from app.dependencies.services import get_indexing_service
# from app.services.IndexingService import IndexingService

# router = APIRouter(
#     prefix="/documents",
#     tags=["Documents"]
# )


# @router.post(
#     "/upload",
#     response_model=UploadResponse,
#     status_code=201,
# )
# async def upload_document(
#     file: UploadFile = File(...),
#     upload_service: UploadService = Depends(
#         get_upload_service
#     )
# ):
#     try:
#         document = upload_service.upload_document(file)

#     except UnsupportedFileType as e:
#         raise HTTPException(
#             status_code=400,
#             detail=str(e)
#         )

#     return UploadResponse(
#         document_id=document.id,
#         filename=document.original_filename,
#         status=document.status,
#         message="Document uploaded successfully."
#     )





# @router.post(
#     "/{document_id}/process",
#     response_model=ProcessingResponse
# )
# async def process_document(
#     document_id: str,
#     indexing_service: IndexingService = Depends(
#     get_indexing_service
# )
# ) -> ProcessingResponse:

#     processed = indexing_service.index_document(document_id)

#     return ProcessingResponse(
#         document_id=document_id,
#         status=DocumentStatus.PROCESSED,
#         page_count=processed.page_count,
#         word_count=processed.word_count,
#         message="Document processed successfully."
#     )








# @router.post(
#     "/chat",
#     response_model=ChatResponse,
# )
# def chat(
#     request: ChatRequest,
#     chat_service: ChatService = Depends(
#         get_chat_service,
#     ),
    
# ) -> ChatResponse:

#     answer = chat_service.chat(
#         question=request.question,
#         document_id=request.document_id,
#     )

#     return ChatResponse(
#         answer=answer,
#     )




router = APIRouter()

@router.get("/")
def test():
    return {"status": "ok"}