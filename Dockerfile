FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements_for_docker.txt /code/
RUN pip install -r requirements_for_docker.txt
COPY . /code/