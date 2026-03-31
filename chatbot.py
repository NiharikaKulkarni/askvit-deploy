import faiss
import pickle
from sentence_transformers import SentenceTransformer
from groq import Groq

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index and chunks
index = faiss.read_index("faiss_index/index.faiss")
chunks = pickle.load(open("faiss_index/chunks.pkl", "rb"))

# Initialize LLM client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_bot(query):
    # Step 1: Convert question to vector
    query_vector = embed_model.encode([query])

    # Step 2: Semantic search in FAISS
    distances, indices = index.search(query_vector, 3)

    # Step 3: Retrieve relevant text
    context = ""
    for i in indices[0]:
        context += chunks[i].page_content + "\n"

    # Step 4: Inject context into prompt
    prompt = f"""
    You are a VIT assistant.
    Answer ONLY using the following information:

    {context}

    Question: {query}
    """

    # Step 5: Generate answer using LLM
    completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "user", "content": prompt}]
)


    return completion.choices[0].message.content
