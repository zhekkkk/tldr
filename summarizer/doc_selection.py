from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import os
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import numpy as np

def create_embeddings(docs):
    chunks = [doc.page_content for doc in docs]

    embedder = HuggingFaceInferenceAPIEmbeddings(
        api_key=os.environ.get('HF_TOKEN'),
        model_name="sentence-transformers/all-MiniLM-l6-v2"
    )

    embeddings = embedder.embed_documents(chunks)
    return embeddings

def choose_cluster_number(embeddings):
    max_num_clusters = 15 if len(embeddings) > 14 else len(embeddings) - 1
    k_range = range(4, max_num_clusters)
    silhouette_scores = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(embeddings)
        labels = kmeans.labels_
        score = silhouette_score(embeddings, labels)
        silhouette_scores.append(score)

    optimal_k = k_range[np.argmax(silhouette_scores)]
    return optimal_k

def relevant_chunks_indices(embeddings):
    optimal_k = choose_cluster_number(embeddings)
    clustering = KMeans(n_clusters=optimal_k).fit(embeddings)

    centers = clustering.cluster_centers_
    embeddings = [np.array(emb) for emb in embeddings]

    nearest_indices = []
    for center in centers:
      distances = []
      for i in range(len(embeddings)):
        distance = np.linalg.norm(center - embeddings[i])
        distances.append(distance)
      nearest_indices.append(np.argmin(distances))
    
    return nearest_indices

def select_relevant_docs(docs):
    embeddings = create_embeddings(docs)
    nearest_indices = relevant_chunks_indices(embeddings)
    relevant_docs = [doc for i, doc in enumerate(docs) if i in nearest_indices]
    return relevant_docs