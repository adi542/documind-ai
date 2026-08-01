from app.vectorStores.faiss_vector_store import FaissVectorStore
from app.vectorStores.vector_store import VectorStore


from app.core.config import settings

_vector_store = FaissVectorStore(
    embedding_dimension=settings.EMBEDDING_DIMENSION,
    storage_directory=settings.VECTOR_STORE_DIRECTORY
)

def get_vector_store() -> VectorStore:
    return _vector_store