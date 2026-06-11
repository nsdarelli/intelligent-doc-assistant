from fastapi import FastAPI

app = FastAPI(title="Intelligent Document Assistant")

@app.get("/")
def health():
    return {"status": "healthy"}