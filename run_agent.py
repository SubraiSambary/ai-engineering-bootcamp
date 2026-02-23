from agents.basic_agent import BasicAgent
from core.llm_client import call_llm_json
from core.vector_store import VectorStore
from core.retrieval_service import RetrievalService

if __name__ == "__main__":
    vector_store=VectorStore()

     # Add some test knowledge (optional but useful)
    vector_store.add("doc1", "AWS is a cloud computing platform.")
    vector_store.add("doc2", "The calculator tool performs math operations.")

    retrieval_service = RetrievalService(vector_store)

    agent = BasicAgent(
        goal="What is 25 * 4?",
        llm_client=call_llm_json,
        retrieval_service=retrieval_service
    )    

    agent.run()