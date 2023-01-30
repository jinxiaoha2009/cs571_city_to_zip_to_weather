# cs571_city_to_zip_to_weather
CS571 course home work repo


How to run the program:

Note: please refer to the cs571_lab1.docx for detail process if needed.



Step1: please use ifconfig in macOS or ipconfig in windows to get your local IP address. replace it in /docker1_city_to_zip/app/main.py

IP_ADDRESS = "10.0.0.46"



step 2: build/run two docker containers in two separate terminal:
    Docker1 command:
        docker build -t docker1-city-to-zip . 
        docker run -p 8000:8000 docker1-city-to-zip
    
    Docker2 command:
        docker build -t docker2-zip-to-weather . 
        docker run -p 8001:8001 docker2-zip-to-weather




step 3: open a chrome browser:
    http://localhost:8000/city/sunnyvale

    the result is: {"weather":"good"}

    http://localhost:8000/city/mtv
    the result is: {"weather":"bad"}

    other city will return {"weather":"unkown"}





