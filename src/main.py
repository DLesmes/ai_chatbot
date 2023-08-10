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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)