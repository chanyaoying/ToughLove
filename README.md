# ToughLove

## Prerequisites
- Python 3.7 (only)
- Docker & Docker Compose (not required, but highly recommended)
- At least 3 GB of free disk space

## Installation
Get the models from [Google Drive](https://drive.google.com/drive/u/0/folders/1P3ulE3qHqupbvsDr4khC346VZzyiAmyY). 


Unzip the models and put them in the appropirate locations. Use `#` as a guide. It should look like this:
```
Folder structure:

project root
|
|--- models
|    |--- insult
|    |    |--- insult.py
|    |    |--- checkpoint (gpt-2 model here)
|    |    |    |--- # run 1 (or run 2)
|    |    |    
|    |    |--- Models (bert and bart models unzipped here)
|    |    |    |--- # fintuned_bert
|    |    |    |--- # fintuned_bart
|    |
|    |--- intent
|    |--- |--- intent.py
|    |--- |--- requirements.txt
|    |--- |--- user_input_classifier
|    |--- |--- | --- ...
|    |
|    |--- social
|    |--- |--- # chatbot run 1.h5 (or 2, 3)
|    |--- |--- # tokenizer_v2.pkl (or ...)
|    |--- |--- preprocessing.py
|    |--- |--- requirements.txt
|    |--- |--- social.py
|    |--- |--- util.py
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
|
```
## Using Python Virtual Environment
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

## Using Docker
Run docker compose up
```
docker-compose up
```

When switching out models, rebuild the docker images
```
docker-compose up --build
```