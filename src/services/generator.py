"""generator module"""

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from fastapi import status
from fastapi.responses import JSONResponse
from clients.llm import OpenAssistant
openassistant = OpenAssistant()


class Generator:
    """
    A class for generating chat responses using the provided prompt.

    # Args:
    #     openassistant: An instance of the OpenAssistant class for generating chat completions.
    """

    def answer(self, prompt):
        """
        Generate a answer response using the provided prompt.

        Args:
            prompt (str): The input data containing the prompt.
            # max_steps (int, optional): Maximum number of steps for chat generation. Default is 4096.

        Returns:
            str: A generated chat response.
        """
        try:
            max_steps=2048 * 2
            input_prompt = f"<|prompter|>{prompt}<|endoftext|><|assistant|>"
            for _ in range(max_steps):
                completion = openassistant.completer(input_prompt)
                return completion
        except Exception as ex:
            error_info = f"Error when executing Generator.chat: {ex}"
            logging.error(error_info)
            return JSONResponse(
                content=error_info, status_code=status.HTTP_424_FAILED_DEPENDENCY
            )
