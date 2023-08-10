"""generator module"""

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from fastapi import status
from fastapi.responses import JSONResponse
from schemas.message import body
from clients import OpenAssistant
openassistant = OpenAssistant()

class Generator:
    """
    A class for generating chat responses using the provided prompt.

    Args:
        openassistant: An instance of the OpenAssistant class for generating chat completions.
    """

    def __init__(self, openassistant):
        self.openassistant = openassistant

    def answer(self, body, max_steps=2048 * 2):
        """
        Generate a answer response using the provided prompt.

        Args:
            body (object): The input data containing the prompt.
            max_steps (int, optional): Maximum number of steps for chat generation. Default is 4096.

        Returns:
            str: A generated chat response.
        """
        try:
            input = f"<|prompter|>{body.prompt}<|endoftext|><|assistant|>"
            for _ in range(max_steps):
                completion = self.openassistant.completer(input)
                return completion
        except Exception as ex:
            error_info = f"Error when executing Generator.chat: {ex}"
            logging.error(error_info)
            return JSONResponse(
                content=error_info, status_code=status.HTTP_424_FAILED_DEPENDENCY
            )
