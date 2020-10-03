FROM python:3.8.5-slim-buster

COPY . /cli

WORKDIR /cli

RUN pip install .

ENTRYPOINT ["nlp-cli"]