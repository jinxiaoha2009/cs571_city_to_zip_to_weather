from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

IP_ADDRESS = "10.0.0.46"

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/city/{cityname}")
async def get_zipcode(cityname: str):
    zipcode = "00000"
    if cityname == "sunnyvale":
        zipcode = "94085"
    elif cityname == "mtv":
        zipcode = "94035"
    else:
        zipcode = "00000"

    url = f"http://{IP_ADDRESS}:8001/ziptoweather/{zipcode}"
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
