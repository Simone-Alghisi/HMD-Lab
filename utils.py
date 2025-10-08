from typing import Any, Callable, Dict, Tuple
from functools import partial

from transformers import AutoModelForCausalLM

from models import qwen3

# You can add more models here as needed
# The tuple contains the model name, a partial function with the model specific arguments, the method to prepare the input text
MODELS: Dict[str, Tuple[str, Callable[..., Any], Callable[..., Any]]] = {
    "qwen3": (
        "Qwen/Qwen3-4B-Instruct-2507",
        partial(AutoModelForCausalLM.from_pretrained, trust_remote_code=True),
        qwen3.prepare_text,
    )
}
