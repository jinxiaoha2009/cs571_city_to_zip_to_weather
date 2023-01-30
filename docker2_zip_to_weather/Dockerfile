FROM python:3.8

WORKDIR /zip-to-weather-app

COPY dependency.txt .

RUN pip install -r dependency.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]

# docker build -t docker2-zip-to-weather . 
# docker run -p 8001:8001 docker2-zip-to-weather