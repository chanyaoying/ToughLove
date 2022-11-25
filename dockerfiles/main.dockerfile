FROM python:3.7-slim-buster

# Create app directory
WORKDIR /usr/src/app/

# Create virtual environment
RUN python -m venv venv
ENV PATH="/usr/src/app/venv/bin:$PATH"

# Install app dependencies
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# Copy app
COPY ./main.py ./
COPY ./util.py ./

# Run
# RUN export FLASK_APP=main
EXPOSE 5000

CMD ["python", "main.py"]
# CMD [ "gunicorn", "-b", ":8000", "main:app"]