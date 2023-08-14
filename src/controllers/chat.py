""" chat module """

from starlette.responses import StreamingResponse
from fastapi import APIRouter
from schemas.message import Body
from services.generator import Generator
generator = Generator()


router = APIRouter()

@router.post("/chat",
    description="""# Generate

Request an answer for the LLM
    """,
    tags=["Chat"]
)
async def generate(body: Body):
    content = generator.answer(prompt=body.prompt)
    return StreamingResponse(
            content=content,
            media_type="text/plain"
        )