import fastapi
import os
import uvicorn

app = fastapi.FastAPI()

@app.get("/test", status_code=200)
async def get_health() -> dict:
    return {
        "status": True
    }

@app.get("/health", status_code=200)
async def get_health() -> dict:
    return {
        "status": "OK"
    }

@app.post("/predict", status_code=200)
async def post_predict() -> dict:
    return {
        'status': True
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Default to 8080 if PORT isn’t set
    uvicorn.run(app, host="0.0.0.0", port=port)