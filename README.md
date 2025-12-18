## RAG-based-Medical-Knowledge-Assistant

A Retrieval-Augmented Generation (RAG) system for medical question answering, built using authoritative reference material from the Gale Encyclopedia of Medicine. The system retrieves relevant medical context using semantic search and generates responses grounded in retrieved source content.

### Overview:

Large Language Models may generate responses that are not aligned with domain-specific knowledge. This project addresses that challenge by grounding model outputs in verified medical literature using a Retrieval-Augmented Generation (RAG) architecture. The assistant enables users to ask medical questions and receive context-aware, source-grounded, and domain-specific responses.

### Medical Disclaimer:

This project is for educational and informational use only and is not intended for medical diagnosis or treatment.  
Always consult a qualified healthcare professional for medical advice.

### Intended Use:

The value of this project is in enabling fast, semantic access to large medical reference material. Instead of manually searching textbooks, users can ask natural language questions and receive grounded, source-based explanations.
It is intended for learning, research and informational purposes only and is not designed for diagnosis, treatment, or clinical decision-making.

### System Architecture:

The application follows a standard Retrieval-Augmented Generation pipeline:

- Medical documents are extracted and split into semantic chunks
- Chunks are embedded using a HuggingFace sentence embedding model
- Embeddings are stored in a Pinecone vector database
- User queries are converted into embeddings and matched via similarity search
- Retrieved medical context is passed to the LLM to generate grounded answers

This approach ensures responses are generated based on retrieved medical sources rather than relying solely on the model’s internal knowledge.

### Key Features:

- Domain-specific medical question answering using authoritative reference material
- Semantic search over medical documents using dense vector embeddings
- Retrieval-Augmented Generation to ground LLM responses in source content
- Interactive web interface for real-time medical Q&A
- Containerized deployment with Docker
- Automated CI/CD pipeline using GitHub Actions
- Cloud deployment on AWS EC2

### Tech Stack:
- **Language:** Python 3.12  
- **LLM Orchestration:** LangChain  
- **Embedding Model:** HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`)  
- **Vector Database:** Pinecone  
- **LLM Provider:** Groq (GPT-OSS)  
- **Backend:** Flask  
- **Frontend:** Bootstrap, jQuery  
- **Containerization:** Docker  
- **CI/CD:** GitHub Actions  
- **Cloud Platform:** AWS EC2  

### Getting Started:
#### 1.Clone the repository
```bash
git clone https://github.com/priya-vijayakumar1304/RAG-based-Medical-Knowledge-Assistant.git
cd RAG-based-Medical-Knowledge-Assistant
```
#### 2.Create and activate a virtual environment
```bash
conda create -p venv python==3.12.7 -y
conda activate venv/
```
#### 3.Install dependencies
```bash
pip install -r requirements.txt
```
#### 4.Configure environment variables
Create a .env file in the project root:
```
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```
#### 5.Index medical documents into Pinecone
```
python store_index.py
```
#### 6.Run the application
```
python app.py
```
Open your browser and navigate to:
```
http://localhost:8080
```

### Deployment (AWS + CI/CD):
This project supports automated deployment using Docker and GitHub Actions.

#### Deployment Flow:
1.Build Docker image from source code

2.Push image to Amazon ECR

3.Deploy container on AWS EC2

4.Automate builds and deployments via GitHub Actions

#### Required GitHub Secrets:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `ECR_REPO`
- `PINECONE_API_KEY`
- `GROQ_API_KEY`

### Future Enhancements:

- **Hybrid Retrieval:** Combine dense vector search with keyword-based retrieval (BM25) to improve recall for complex and rare medical queries  
- **Reranking:** Introduce a reranking layer (e.g., cross-encoders or LLM-based rerankers) to improve relevance of retrieved context before generation  
- **Citation Display:** Surface source references (document sections or pages) alongside generated responses for improved transparency  
- **Multi-Document Ingestion:** Enable dynamic upload and indexing of multiple medical documents beyond the current knowledge base  
- **Response Evaluation:** Integrate automated evaluation techniques to assess response faithfulness and context relevance  

### 📚 Use Cases

- Medical knowledge lookup for students and practitioners
- Reference-based medical Q&A
- AI-powered search over medical textbooks
- Educational and research assistance

### License
This project is licensed under the Apache 2.0 License.

