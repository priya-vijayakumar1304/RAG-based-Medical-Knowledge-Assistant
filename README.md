## RAG-based-Medical-Knowledge-Assistant

An intelligent medical question-answering chatbot built using Retrieval-Augmented Generation (RAG) with the Gale Encyclopedia of Medicine.
The system retrieves relevant medical content from the document, processes it with an LLM, and responds with clean and structured answers.

### Tech Stack
- Python 3.12.7
- LangChain orchestration
- HuggingFaceEmbedding (model: sentence-transformers/all-MiniLM-L6-v2)
- Pinecone Vector Database
- Groq (model: openai/gpt-oss-120b)
- Backend: Flask
- Frontend: Bootstrap + jQuery
- CI/CD pipeline - Github Actions
- Docker
- AWS EC2

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
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
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
   - OPENAI_API_KEY

### 

