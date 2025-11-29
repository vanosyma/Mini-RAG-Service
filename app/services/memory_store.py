from typing import List, Tuple
import numpy as np
from .document_store import DocumentStore

class MemoryDocumentStore(DocumentStore):
    def __init__(self):
        self.docs: List[Tuple[str, list]] = []

    def add(self, text: str, embedding: list) -> int:
        self.docs.append((text, embedding))
        return len(self.docs) - 1

    def search(self, query_embedding: list[float], limit: int = 2) -> List[str]:
        if not self.docs:
            return []

        query = np.array(query_embedding)

        scored = []
        for text, emb in self.docs:
            emb = np.array(emb)
            score = float(np.dot(query, emb) / (np.linalg.norm(query) * np.linalg.norm(emb)))
            scored.append((score, text))

        scored.sort(reverse=True, key=lambda x: x[0])
        return [text for _, text in scored[:limit]]