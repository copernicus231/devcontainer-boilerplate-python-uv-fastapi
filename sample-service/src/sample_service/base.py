from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
