# Mini RAG Service (Refactored Version)


This project demonstrates clean modular architecture, dependency injection, storage abstraction, and maintainable code structure — while preserving the behavior of the original implementation.

---

## 🚀 Features

- Store text documents and generate deterministic embeddings
- Retrieve relevant stored text using cosine similarity
- Simple Question → Answer workflow
- Extensible storage backend:
  - **Memory store (default)**
  - **Optional Qdrant backend (prepared but disabled by default)**
- API automatically documented via FastAPI OpenAPI/Swagger UI

---

## 📁 Project Structure

```
app/
 ├── main.py                 # Application entrypoint
 ├── api/
 │    └── routes.py          # HTTP endpoints
 ├── models/
 │    └── schemas.py         # Request schemas
 ├── services/
 │    ├── embedding_service.py
 │    ├── memory_store.py
 │    ├── qdrant_store.py    # Optional backend
 │    └── rag_service.py
 └── dependencies.py          # Dependency injection
```

The structure follows a clean separation of concerns so the system remains testable, maintainable, and extendable.

---

## 🧩 How to Run

### 1. Install dependencies

```bash
pip install fastapi uvicorn numpy qdrant-client
```

> Qdrant is optional and not required to run the default configuration.

---

### 2. Start the service

From the project root:

```bash
uvicorn app.main:app --reload
```

---

### 3. Open API documentation

```
http://127.0.0.1:8000/docs
```

This provides an interactive UI to test the endpoints.

---

## 🧪 Example Usage

### ➕ Add a document

**POST** `/add`

```
json
{
  "text": "Artificial intelligence enables machines to perform reasoning and learn from data."
}
```

Response:

```
json
{ "id": 0 }
```

---

### ❓ Ask a question

**POST** `/ask`

```
json
{
  "question": "What is artificial intelligence?"
}
```

Example response:

```
json
{
  "answer": "I found this: 'Artificial intelligence enables machines to perform reasoning and learn from data....'",
  "context": [
    "Artificial intelligence enables machines to perform reasoning and learn from data."
  ]
}
```

---

## 🔧 Backend Mode

| Mode | Status | Notes |
|------|--------|-------|
| Memory Store | **Enabled by default** | Lightweight and ideal for evaluation/testing |
| Qdrant Store | Available (disabled) | Can be activated for vector DB support |

The service is designed so storage implementation can be replaced without modifying routes or business logic.

---

## 🧠 Architecture Principles Applied

- Separation of concerns
- Strategy pattern for storage
- Dependency injection
- Behavior parity with original implementation
- Extensible modular design

---

## 📄 Notes for Reviewers

This project was refactored with the intention to improve structure and scalability without modifying existing API behavior, as aligned with the assessment requirements.  
Additional reasoning and design notes can be found in:

```
notes.md
```

---

## 📬 Contact

For questions or clarification regarding this submission, feel free to reach out.

---

