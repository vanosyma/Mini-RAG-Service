from typing import Protocol, List

class DocumentStore(Protocol):
    def add(self, text: str) -> int:
        ...

    def search(self, query_embedding: list[float], limit: int = 2) -> List[str]:
        ...