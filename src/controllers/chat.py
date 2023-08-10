""" chat module """

from starlette.responses import StreamingResponse
from fastapi import APIRouter
from services.generator import Generator
generator = Generator


router = APIRouter(tags=["Chat"])

@app.post("/")
async def generate(body: Body):
    return StreamingResponse(
            content=generator.answer(body),
            media_type="text/plain"
        )