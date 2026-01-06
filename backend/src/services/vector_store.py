import json
import requests
import io
from PyPDF2 import PdfReader
import os


class VectorStoreMock:
    def __init__(self):
        self.chunks = []  # Each chunk: {text, doc_title, chunk_id, pdf_url, metadata}

    def ingest_from_json_index(self, index_path):
        if not os.path.exists(index_path):
            print(f"WARNING: Document index {index_path} not found, skipping.")
            return
        with open(index_path) as f:
            docs = json.load(f)
        for doc in docs:
            pdf_bytes = None
            try:
                response = requests.get(doc["url"])
                if response.ok:
                    pdf_bytes = response.content
                else:
                    print(f"Failed to download {doc['url']}: {response.status_code}")
                    continue
                reader = PdfReader(io.BytesIO(pdf_bytes))
                for i, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text and text.strip():
                        chunk_id = f"{doc['title']}-page-{i + 1}"
                        self.chunks.append(
                            {
                                "doc_title": doc["title"],
                                "chunk_id": chunk_id,
                                "text": text,
                                "pdf_url": doc["url"],
                                "page": i + 1,
                                "metadata": doc,
                            }
                        )
            except Exception as e:
                print(f"Error loading PDF {doc['url']}: {e}")

    def search(self, query, lang="en", k=5):
        # For demo: keyword relevance scoring (case-insensitive)
        scores = []
        for chunk in self.chunks:
            score = chunk["text"].lower().count(query.lower())
            scores.append((score, chunk))
        scores.sort(reverse=True, key=lambda x: x[0])
        # Return top k chunks with score > 0
        results = [chunk for score, chunk in scores if score > 0][:k]
        return results


vector_store = VectorStoreMock()
