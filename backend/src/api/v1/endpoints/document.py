from src.services.vector_store import vector_store

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

router = APIRouter()


@router.on_event("startup")
def load_documents():
    # Loads on API startup
    import os

    index_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), "../../../models/document_index_en.json"
        )
    )
    print(f"[DEBUG] Looking for document index at {index_path}")
    vector_store.ingest_from_json_index(index_path)
    print(f"Loaded {len(vector_store.chunks)} document chunks.")


@router.get("/document/search")
def document_search(q: str = Query(...), lang: str = Query("en")):
    results = vector_store.search(q, lang)
    # Return chunk previews and doc metadata
    preview = [
        {
            "doc_title": r["doc_title"],
            "pdf_url": r["pdf_url"],
            "page": r["page"],
            "chunk_id": r["chunk_id"],
            "snippet": r["text"][:400],
            "metadata": r["metadata"],
        }
        for r in results
    ]
    return JSONResponse(preview)


@router.post("/document/ask")
def document_qa(q: str = Query(...), lang: str = Query("en")):
    # For demo: Retrieve top chunks and concatenate as answer
    results = vector_store.search(q, lang)
    answer = "\n---\n".join(r["text"] for r in results)
    return JSONResponse(
        {
            "answer": answer,
            "sources": [
                {
                    "doc_title": r["doc_title"],
                    "pdf_url": r["pdf_url"],
                    "page": r["page"],
                    "chunk_id": r["chunk_id"],
                }
                for r in results
            ],
        }
    )
