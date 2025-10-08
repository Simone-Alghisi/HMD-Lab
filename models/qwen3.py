from typing import Dict, List, Optional

from transformers import PreTrainedTokenizer


def prepare_text(
    prompt,
    tokenizer: PreTrainedTokenizer,
    messages: Optional[List[Dict[str, str]]] = None,
    n_exchanges: int = 2,
):
    if messages is None:
        messages = []
    messages.append({"role": "user", "content": prompt})

    text = tokenizer.apply_chat_template(
        messages[-n_exchanges * 2 :],
        tokenize=False,
        add_generation_prompt=True,
    )

    return text
