from fastapi import APIRouter, Depends
from ..models.schemas import QuestionRequest, DocumentRequest
from ..dependencies import get_rag

router = APIRouter()

@router.post("/ask")
def ask(req: QuestionRequest, rag=Depends(get_rag)):
    return rag.retrieve_answer(req.question)

@router.post("/add")
def add(req: DocumentRequest, rag=Depends(get_rag)):
    return {"id": rag.add_document(req.text)}