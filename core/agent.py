from typing import List, Dict, Any
from core.retrieval_service import RetrievalService

class SimpleAgent:
    def __init__(self, retrieval_service: RetrievalService):
        self.retrieval_service = retrieval_service

    def run(self, query: str, top_k: int = 3) -> Dict[str, Any]:
        #Step1 :Retrieve relevant documents
        retrieved_docs = self.retrieval_service.retrieve(query, top_k=top_k)
        
        # Step 2: Build context (for future LLM reasoning)
        context="\n\n".join(
            [doc["text"] for doc in retrieved_docs]
        )

        # Step 3: Return structured output
        return {
            "query": query,
            "retrieved_documents": retrieved_docs,
            "context": context
        }