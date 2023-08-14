""" main file calling the controllers module"""
# uvicorn
import uvicorn
from fastapi import FastAPI
from controllers import chat

# settings
from settings import Settings
settings = Settings()


app = FastAPI(
    title="AI Chatbot - A chat bot powered by a Open Source LLM",
    root_path=settings.ROOT_PATH,
)

app.include_router(chat.router)


@app.get("/", summary="Health check", status_code=200, tags=["Check Health"])
async def health():
    """Health check endpoint"""
    return {"health": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
