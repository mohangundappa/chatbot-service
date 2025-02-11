from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.chatbot.config import settings
from chatbot.api.routes import router

app = FastAPI(
    title="Chatbot API",
    version="1.0.0",
    description="Handles external chat ID to thread ID mapping for persistent conversations",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "environment": settings.app_env,
        "model": settings.model_name
    }