"""generator module"""

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from fastapi import status
from fastapi.responses import JSONResponse
from schemas.message import body
from clients import OpenAssistant
openassistant = OpenAssistant()

class Generator():

    def chat(
        body,
        max_steps = 2048*2
    ):
        try:
            input = f"<|prompter|>{body.prompt}<|endoftext|><|assistant|>"
            for _ in range(max_steps):
                completion = openassistant.completer(input)
                return completion
        except Exception as ex:
            error_info = f"Error when executing Generator.chat: {ex}"
            logging.error(error_info)
            return JSONResponse(
                content=error_info, status_code=status.HTTP_424_FAILED_DEPENDENCY
            )
            
        
