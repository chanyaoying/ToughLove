FROM python:3.7-slim-buster

# Create app directory
WORKDIR /usr/src/app/

# copy depedenencies from main.dockerfile
COPY --from=yaoyingsmu/toughlove_main:latest /usr/src/app/venv /usr/src/app/venv
ENV PATH="/usr/src/app/venv/bin:$PATH"

# Copy app
COPY ./models/intent ./

# Install additional dependencies
RUN . /usr/src/app/venv/bin/activate && pip install -r requirements.txt

# Run
EXPOSE 5002

CMD . /usr/src/app/venv/bin/activate && python intent.py
