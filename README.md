# ToughLove

## Prerequisites
- Docker & Docker Compose (not required, but **very** highly recommended)
- At least 13 GB *(edit: used to say 3 GB)* of free disk space
- Python 3.7.15 (only if not using Docker)


## Installation

It is much much much easier to use Docker Compose to run the backend. If you don't have Docker Compose, you can install it from [here](https://docs.docker.com/compose/install/).

### Using Docker
Not much time and computing power should be needed to spin up the backend. The first time you run the backend, it will take a while to download the Docker images from Docker Hub. After that, it should be pretty quick.

Run docker compose up
```
docker-compose up
```

When switching out models, rebuild the docker images
```
docker-compose up --build
```

### Using Python Virtual Environment
Get the models from [Google Drive](https://drive.google.com/drive/u/0/folders/1P3ulE3qHqupbvsDr4khC346VZzyiAmyY). 


Unzip the models and put them in the appropirate locations. Use `#` as a guide. It should look like this:
```
Folder structure:

project root
|
|--- models
|    |
|    |--- insult
|    |    |
|    |    |--- insult.py
|    |    |
|    |    |--- checkpoint (gpt-2 model here)
|    |    |    |
|    |    |    |--- # run 1 (or run 2)
|    |    |    
|    |    |--- Models (bert and bart models unzipped here)
|    |         |
|    |         |--- # fintuned_bert
|    |         |--- # fintuned_bart
|    |
|    |
|    |--- intent
|    |    |
|    |    |--- intent.py
|    |    |--- requirements.txt
|    |    |
|    |    |--- user_input_classifier
|    |         | --- ...
|    |
|    |
|    |--- social
|         |
|         |--- # chatbot run 1.h5 (or 2, 3)
|         |--- # tokenizer_v2.pkl (or ...)
|         |--- preprocessing.py
|         |--- requirements.txt
|         |--- social.py
|         |--- util.py
|
|
|--- .gitignore
|--- LICENSE
|--- main.py
|--- test.py
|--- README.md
|--- requirements.txt
|--- base_requirements.txt
|--- util.py
|--- versions.txt
|--- docker-compose.yml
|--- dockerfiles
|    |--- ...
```

Create a virtual environment and activate it:
```
python3 -m venv venv && source venv/bin/activate
```

or if you are using Windows OS
```
python -m venv venv && venv\Scripts\activate
```

Install the requirements. Windows users can use `pip` instead of `pip3`:
```
pip3 install -r base_requirements.txt
```

Run the program. Windows users can use `python` instead of `python3`:
```
python3 main.py
```

## Usage

### Testing the API
Upon installation, check that the backend is running by going to `localhost:5000` in your browser. You should see a message that says `ToughLove API is running.`. If you see this, then the orchestrator is running.

### Testing that the microservices are working
Run this command to test that the microservices are working:
```bash
curl "http://localhost:5000/test"
```

You should receive a response that looks like this:
```json
{
    "insult": "Insult API is running.",
    "intent": "Intent Classifier API is running.",  "social":"Social chatbot API is running."
}
```
### Using with the frontend
The frontend is located [here](https://github.com/Rdice14/chat-ui). Instructions on how to run the frontend can be found in the README.md file in the frontend repository.
