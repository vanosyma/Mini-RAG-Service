from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from typing import List
from .document_store import DocumentStore


class QdrantDocumentStore(DocumentStore):
    def __init__(self):
        self.client = QdrantClient("http://localhost:6333")
        self.collection = "demo_collection"

        self.client.recreate_collection(
            collection_name=self.collection,
            vectors_config=VectorParams(size=128, distance=Distance.COSINE)
        )

    def add(self, text: str, embedding=None) -> int:
        doc_id = abs(hash(text)) % 100_000_000
        self.client.upsert(
            collection_name=self.collection,
            points=[PointStruct(id=doc_id, vector=embedding, payload={"text": text})]
        )
        return doc_id

    def search(self, query_embedding: list[float], limit: int = 2) -> List[str]:
        hits = self.client.search(collection_name=self.collection, query_vector=query_embedding, limit=limit)
        return [hit.payload["text"] for hit in hits]