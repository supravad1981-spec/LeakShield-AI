from fastapi import FastAPI

app = FastAPI(
    title="LeakShield AI",
    description="AI-powered question paper leak detection system",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "LeakShield AI Backend Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
