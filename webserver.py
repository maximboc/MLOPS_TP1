from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.get("/predict")
async def predict():
    return JSONResponse(content={"y_pred": 2})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
