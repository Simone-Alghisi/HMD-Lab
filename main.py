import argparse
from argparse import ArgumentParser

import torch
from transformers import AutoTokenizer

from utils import MODELS


def parse_args() -> argparse.Namespace:
    parser = ArgumentParser(
        prog="python -m main",
        description="Interact with a language model.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--model-name",
        type=str,
        choices=MODELS.keys(),
        default="qwen3",
        help="Name of the model to use.",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda:0" if torch.cuda.is_available() else "cpu",
        help="Device to run the model on.",
    )
    parser.add_argument(
        "--n-exchanges",
        type=int,
        default=2,
        help="Number of exchanges to keep in the conversation history.",
    )
    return parser.parse_args()


def interact(args: argparse.Namespace) -> None:
    """A simple function to interact with the model."""
    model_name, InitModel, prepare_text = MODELS[args.model_name]

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = InitModel(
        model_name,
        dtype="auto",
        device_map=args.device,
    )

    messages = [
        {
            "role": "system",
            "content": f"Hello! You are using {args.model_name}. How can I help you today?",
        }
    ]
    while True:
        user_input = input(f"System: {messages[-1]['content']}\nUser: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        # prepare the model input
        text = prepare_text(user_input, tokenizer, messages, args.n_exchanges)
        model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

        with torch.no_grad():
            generated_ids = model.generate(**model_inputs, max_new_tokens=16384).cpu()

        # decode the output
        output_ids = generated_ids[0][len(model_inputs.input_ids[0]) :].tolist()
        content = tokenizer.decode(output_ids, skip_special_tokens=True)
        messages.append({"role": "system", "content": content})


if __name__ == "__main__":
    args = parse_args()
    interact(args)
