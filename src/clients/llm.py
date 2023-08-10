""" Calling the LLM """
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from transformers import (
    AutoTokenizer,
    GPTNeoXForCausalLM
)

class OpenAssistant:
    """
    A class for interacting with the OpenAssistant language model.

    Args:
        max_new_tokens (int, optional): Maximum number of new tokens to generate. Default is 3.
        do_sample (bool, optional): Whether to use sampling for token generation. Default is True.
        temperature (float, optional): Sampling temperature for token generation. Default is 0.9.
        top_k (int, optional): Value for top-k sampling. Default is 50.
        top_p (float, optional): Value for nucleus sampling. Default is 0.9.
        repetition_penalty (float, optional): Repetition penalty for token generation. Default is 1.2.
    """

    def __init__(
            self,
            max_new_tokens: int = 3,
            do_sample: bool = True,
            temperature: float = 0.9,
            top_k: int = 50,
            top_p: float = 0.9,
            repetition_penalty: float = 1.2,
            return_tensors: str = "pt",
            checkpoint: str = "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5",
            cache_dir: str = '/cache'
    ):
        self.checkpoint = checkpoint
        self.cache_dir = cache_dir
        self.max_new_tokens = max_new_tokens
        self.do_sample = do_sample
        self.temperature = temperature
        self.top_k = top_k
        self.top_p = top_p
        self.repetition_penalty = repetition_penalty
        self.return_tensors = return_tensors

    def loader(self):
        """
        Load the tokenizer and model for the OpenAssistant.

        Returns:
            tuple: A tuple containing the tokenizer and model.
        """
        logging.info("Loading Model...")
        tokenizer = AutoTokenizer.from_pretrained(
            checkpoint=self.checkpoint,
            cache_dir=self.cache_dir
        )
        model = GPTNeoXForCausalLM.from_pretrained(
            checkpoint=self.checkpoint,
            cache_dir=self.cache_dir,
            device_map="auto"
        ).half()
        logging.info("Model loaded!")
        return tokenizer, model

    def completer(self, input_text):
        """
        Generate a completion for the given input text.

        Args:
            input_text (str): The input text to complete.

        Yields:
            str: A generated completion response.
        """
        tokenizer, model = self.loader()
        inputs = tokenizer(
            input_text,
            return_tensors="pt"
        )
        inputs.to(0)
        tokens = model.generate(
            **inputs,
            max_new_tokens=self.max_new_tokens,
            do_sample=self.do_sample,
            temperature=self.temperature,
            top_k=self.top_k,
            top_p=self.top_p,
            repetition_penalty=self.repetition_penalty
        )
        generated_text = tokenizer.decode(tokens[0])
        response = generated_text.split()[-1].split()[0]
        if generated_text.endswith(' '):
            yield response