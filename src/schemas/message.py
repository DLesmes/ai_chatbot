""" message module """

from pydantic import BaseModel

class Body(BaseModel):
    prompt: str