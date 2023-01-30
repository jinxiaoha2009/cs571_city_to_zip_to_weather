FROM python:3.8

WORKDIR /city-to-zip-app

COPY dependency.txt .

RUN pip install -r dependency.txt

COPY ./app ./app

CMD ["python", "./app/main.py"]

# docker build -t docker1-city-to-zip . 
# docker run -p 8000:8000 docker1-city-to-zip