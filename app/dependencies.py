from .services.embedding_service import EmbeddingService
from .services.memory_store import MemoryDocumentStore
from .services.qdrant_store import QdrantDocumentStore
from .services.rag_service import RagService

_store = MemoryDocumentStore()
_embedder = EmbeddingService()
_rag = RagService(store=_store, embedder=_embedder)

def get_store():
    return _store

def get_rag():
    return _rag
