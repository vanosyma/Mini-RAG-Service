from .embedding_service import EmbeddingService
from .document_store import DocumentStore

class RagService:
    def __init__(self, store: DocumentStore, embedder: EmbeddingService):
        self.store = store
        self.embedder = embedder

    def add_document(self, text: str) -> int:
        emb = self.embedder.create_embedding(text)
        return self.store.add(text, emb)


    def retrieve_answer(self, question: str) -> dict:
        emb = self.embedder.create_embedding(question)
        results = self.store.search(emb)

        if results:
            return {
                "answer": f"I found this: '{results[0][:100]}...'",
                "context": results
            }
        return {"answer": "Sorry, I don't know.", "context": []}