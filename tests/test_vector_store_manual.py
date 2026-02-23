from core.vector_store import VectorStore   

def test_vector_store_ranking():
    store = VectorStore()

    store.add("r1","Built scalable AWS cloud infrastructure")
    store.add("r2","Developed frontend applications using React")
    store.add("r3","Managed Kubernetes clusters and Docker containers")

    results = store.search(
        "Looking for cloud architecture and AWS experience",
        top_k=1
        )  

    assert results[0]["id"] == "r1"
    assert results[0]["score"] > 0.5