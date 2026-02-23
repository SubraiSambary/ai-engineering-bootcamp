from core.vector_store import VectorStore
from core.retrieval_service import RetrievalService

def test_retrieval_service():
    store = VectorStore()

    store.add("r1","Built scalable AWS cloud infrastructure")
    store.add("r2","Developed frontend applications using React")
    store.add("r3","Managed Kubernetes clusters and Docker containers")

    retrieval = RetrievalService(store)    
    results = retrieval.retrieve(
        "Looking for cloud architecture and AWS experience",
        top_k=1
        )  

    assert results[0]["id"] == "r1"