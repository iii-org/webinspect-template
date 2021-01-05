# FROM 10.50.1.63:5443/dockerhub/library/python:3.8-alpine3.11
FROM python:3.8-alpine3.11
WORKDIR /usr/src/app
COPY . .
RUN pip install -i https://pypi.douban.com/simple flask
CMD [ "python", "main.py"]

