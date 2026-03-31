**Deployment Purpose version of askVIT — RAG-Based Academic Assistant**
askVIT is a domain-specific academic assistant that answers student queries using Retrieval-Augmented Generation (RAG) grounded in institutional documents. The system retrieves relevant content from official PDFs and generates responses based only on that context to ensure reliability and reduce hallucinations.

**Overview**
Students often struggle to find accurate academic information because official guidelines are distributed across multiple documents. This project addresses that problem by indexing institutional PDFs and enabling semantic search and context-aware responses through a retrieval-based architecture.

**Key Features**
Domain-constrained academic chatbot
Retrieval-Augmented Generation pipeline
Semantic search using vector embeddings
Context-grounded responses
Query history support
Suggested queries interface
Fallback response when information is unavailable
Scalable document ingestion

**Architecture**
Query → Embedding → Vector Search → Relevant Chunks → Response Generation

**Tech Stack**
Language: Python
Frameworks/Libraries: Streamlit, LangChain, FAISS
Document Processing: PyPDFLoader, text splitting utilities
Frontend: Streamlit UI with custom styling

**Workflow**
Documents are loaded and parsed.
Text is split into smaller chunks.
Chunks are converted into embeddings.
Embeddings are stored in a vector index.
User queries are embedded and compared.
Relevant chunks are retrieved.
The model generates an answer grounded in retrieved context.

**Evaluation Approach**
Responses are validated by checking whether generated answers are supported by retrieved document content. If relevant context is not found, the system returns a fallback response instead of generating unsupported answers.

**Limitations**
Requires re-indexing when new documents are added
Dependent on document quality
No automated evaluation metrics yet
Retrieval accuracy depends on chunk configuration

**Future Work**
Hybrid search (keyword + vector)
Confidence scoring
Source citation display
Incremental indexing
Support for multiple institutions

**Author
Niharika Santosh Kulkarni
Integrated M.Tech Software Engineering — VIT**
