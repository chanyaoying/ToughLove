FROM python:3.7-slim-buster

# Create app directory
WORKDIR /usr/src/app/

# Install app dependencies
COPY ../models/social/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN export FLASK_APP=social

# Run
EXPOSE 5001
COPY ../models/social/chatbot.h5 ./
COPY ../models/social/tokenizer_v0(chatbot.h5).pkl ./
COPY ../models/social/social.py ./
COPY ../models/social/preprocessing.py ./
COPY ../models/social/util.py ./
CMD [ "gunicorn", "-b", "0.0.0.0:5001", "social:app", "-w", "4"]