from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/city/{cityname}")
def get_zipcode(cityname: str):
    if cityname == "sunnyvale":
        return {"zipcode": "94085"}
    elif cityname == "mtv":
        return {"zipcode": "94035"}
    
    else:
        return {"zipcode": "unknown"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
