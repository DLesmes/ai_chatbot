""" message module """

from pydantic import BaseModel
from utils.samples import basic_prompt


class Body(BaseModel):
    prompt: str

    class Config:
        schema_extra = {"example": basic_prompt}
