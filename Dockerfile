FROM python:3.8.5-alpine3.12

RUN apk update && apk add curl

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

RUN pip install -r requirements.txt

RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && echo Asia/Seoul > /etc/timezone

# execute the Flask app
CMD ["python", "app.py"]
