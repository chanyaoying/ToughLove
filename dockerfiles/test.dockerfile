FROM python:3.7-slim-buster

# Create app directory
WORKDIR /usr/src/app/

# copy depedenencies from main.dockerfile
COPY --from=yaoyingsmu/toughlove_main:latest /usr/src/app/venv /usr/src/app/venv
ENV PATH="/usr/src/app/venv/bin:$PATH"

# Copy app
COPY ./test.py ./
COPY ./util.py ./

# Run
# RUN export FLASK_APP=test
EXPOSE 5001

CMD ["python", "test.py"]
# CMD [ "gunicorn", "-b", ":8001", "test:app", "-w", "2", "--threads", "4", "--worker-class", "gthread"]