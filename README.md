## RAG-based-Medical-Knowledge-Assistant

A Retrieval-Augmented Generation (RAG) system for medical question answering, built using authoritative reference material from the Gale Encyclopedia of Medicine. The system retrieves relevant medical context using semantic search and generates responses grounded in retrieved source content.

### Overview

Large Language Models may generate responses that are not aligned with domain-specific knowledge. This project addresses that challenge by grounding model outputs in verified medical literature using a Retrieval-Augmented Generation (RAG) architecture. The assistant enables users to ask medical questions and receive context-aware, source-grounded, and domain-specific responses.

### Medical Disclaimer

This project is for educational and informational use only and is not intended for medical diagnosis or treatment.  
Always consult a qualified healthcare professional for medical advice.

### Intended Use

The value of this project is in enabling fast, semantic access to large medical reference material. Instead of manually searching textbooks, users can ask natural language questions and receive grounded, source-based explanations.
It is intended for learning, research and informational purposes only and is not designed for diagnosis, treatment, or clinical decision-making.

### System Architecture

The application follows a standard Retrieval-Augmented Generation pipeline:

- Medical documents are extracted and split into semantic chunks
- Chunks are embedded using a HuggingFace sentence embedding model
- Embeddings are stored in a Pinecone vector database
- User queries are converted into embeddings and matched via similarity search
- Retrieved medical context is passed to the LLM to generate grounded answers

This approach ensures responses are generated based on retrieved medical sources rather than relying solely on the model’s internal knowledge.

### Key Features

- Domain-specific medical question answering using authoritative reference material
- Semantic search over medical documents using dense vector embeddings
- Retrieval-Augmented Generation to ground LLM responses in source content
- Interactive web interface for real-time medical Q&A
- Containerized deployment with Docker
- Automated CI/CD pipeline using GitHub Actions
- Cloud deployment on AWS EC2

### Tech Stack
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

### How to run?
#### STEPS:

Clone the repository

```bash
git clone https://github.com/priya-vijayakumar1304/RAG-based-Medical-Knowledge-Assistant.git
```
#### STEP 01- Create a conda environment after opening the repository

```bash
conda create -p venv python==3.12.7 -y
```

```bash
conda activate venv/
```


#### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


#### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
GROQ_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```

### AWS-CICD-Deployment-with-Github-Actions

#### 1. Login to AWS console.

#### 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Launch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
#### 3. Create ECR repo to store/save docker image (save the respository URI)
	
#### 4. Create EC2 machine (Ubuntu) 

#### 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
#### 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


#### 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   - PINECONE_API_KEY
   - GROQ_API_KEY

### 

