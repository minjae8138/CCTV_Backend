FROM python:3.8.5-buster
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install tensorflow --upgrade --force-reinstall
