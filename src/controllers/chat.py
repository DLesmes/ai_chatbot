""" chat module """

from starlette.responses import StreamingResponse
from fastapi import APIRouter
from schemas.message import Body
from services.generator import Generator
generator = Generator


router = APIRouter(tags=["Chat"])

@router.post("/")
async def generate(body: Body):
    return StreamingResponse(
            content=generator.answer(body),
            media_type="text/plain"
        )