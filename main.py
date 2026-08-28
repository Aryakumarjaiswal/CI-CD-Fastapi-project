from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "FastAPI App is running live!"}

@app.get("/health")
def health_check():
    return {"health": "healthy"}
