# Technical Notes

## 1. Overview

The goal of this refactor was to improve the structure, maintainability, and extensibility of the original implementation without modifying its external behavior. The application still supports:

- Storing text documents
- Generating deterministic embeddings
- Retrieving relevant documents based on similarity
- Producing a simple RAG-style response

The refactor focuses solely on code organization and architectural clarity rather than adding or changing functionality.

---

## 2. Design Decisions

### 2.1 Separation of Concerns

The codebase was reorganized into clear, single-purpose modules:

| Layer | Responsibility |
|-------|---------------|
| `api/` | Defines HTTP routes without business logic |
| `services/` | Contains core business logic (embedding, retrieval, storage) |
| `models/` | Defines request validation schemas via Pydantic |
| `dependencies.py` | Manages dependency lifecycle and injection |
| `main.py` | Application entry point (kept intentionally minimal) |

This separation gives the project a structure suitable for scaling and testing.

---

### 2.2 Storage Abstraction (Strategy Pattern)

A `DocumentStore` protocol defines the expected interface for storage.  
Two interchangeable implementations are available:

- `MemoryDocumentStore` — default mode (stateless demo / local testing)
- `QdrantDocumentStore` — prepared for future production-grade vector DB usage

With this approach, the storage mechanism can be swapped with no changes to the API layer.

---

### 2.3 Dependency Injection

Instead of instantiating services directly inside routes, the application uses dependency functions that provide shared, singleton-like instances. This ensures:

- persistence across requests
- cleaner testing and mocking
- predictable system state

FastAPI's dependency system made this pattern natural and lightweight.

---

### 2.4 Deterministic Embedding Logic

Embeddings are implemented using deterministic pseudo-random values based on hashing.  
This preserves the semantic search concept while keeping the environment lightweight and dependency-free.

---

## 3. Behavior Preservation

All refactoring work ensured that:

- endpoint paths remained unchanged,
- request/response formats remained identical,
- and application behavior matched the original version.

The refactor improves structure without affecting the interface contract.

---

## 4. Extensibility

The project’s new structure supports future enhancements with minimal friction, such as:

- replacing the embedding generator with a real LLM / ML model,
- enabling or scaling Qdrant storage,
- adding authentication or middleware logging,
- expanding to streaming or long-context architecture.

The system is now aligned with patterns used in production-grade RAG projects.

---

## 5. Trade-offs

| Decision | Trade-off |
|----------|-----------|
| Use memory store by default | No persistence after restart, but ideal for testing |
| Optional Qdrant backend | Additional setup required when activated |
| Deterministic embeddings | Not representative of real semantic models, but predictable and lightweight |

---

## 6. Summary

This refactor focuses on:

- cleaner modular architecture,
- testability and maintainability,
- clear separation between layers,
- backend-agnostic logic,
- and preserved API behavior.

The codebase is now better aligned with modern engineering principles and ready for iterative development or scaling.

---