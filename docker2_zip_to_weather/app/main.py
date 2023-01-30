from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ziptoweather/{zipcode}")
async def get_zipcode(zipcode: str):
    if zipcode == "94085":
        return {"weather": "good"}
    elif zipcode == "94035":
        return {"weather": "bad"}
    else:
        return {"zipcode": "unknown"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
