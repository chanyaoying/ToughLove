# ToughLove

## Prerequisites
- Python >= 3.7, or
- Docker & Docker Compose

## Installation
Unzip the models from google drive <TODO: insert google drive link>. It should look like this:
```
Folder structure:

project root
|
|--- models
|    |--- insult
|    |--- intent
|    |--- social
|
|--- .gitignore
|--- LICENSE
|--- main.py 
|--- README.md
|--- requirements.txt
|--- util.py
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
pip3 install -r requirements.txt
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