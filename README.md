<!-- omit from toc -->
# HMD Lab Repository

Official repository for the [Human-Machine Dialogue (HMD)](https://disi.unitn.it/~riccardi/page7/styled-3/page16.html) course at the University of Trento.

> [!CAUTION]
> For any issue, write an email to s.alghisi@unitn.it and include mahed.mousavi@unitn.it in cc.

- [Getting started](#getting-started)
  - [Installation](#installation)
  - [Create Hugging Face access token](#create-hugging-face-access-token)
- [Running the code](#running-the-code)
  - [Using another model](#using-another-model)
- [License](#license)


## Getting started
This section guides you through the necessary steps to run the code.

### Installation

> [!IMPORTANT]
> Ensure that you have [conda](https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions) installed before proceeding.

Create a Python environment using the following command:
```shell
conda create -n hmd python=3.11
```

In the repository folder, activate the environment and install the required packages:
```shell
conda activate hmd
pip install -r requirements.txt
```

### Create Hugging Face access token
To access models hosted on Hugging Face, create an access token so you can download model checkpoints from the Hugging Face Hub. The steps below will guide you through the process.

> [!TIP]
> If you already have a Hugging Face account, you can skip to step 2.

1. Create an account on [Hugging Face](https://huggingface.co/join)
2. Log in to [Hugging Face](https://huggingface.co/login)
3. [Create a new access token](https://huggingface.co/settings/tokens)

    1. Click on "Create New Access Token"
    2. Select "Read" as the token type
    3. Give it a name, e.g. HMD
    4. Create and "Copy" it, you **won't** be able to do it afterwards

> [!CAUTION]
> You cannot view your token after creating it, so be sure to copy it immediately.
>
> *If you lose it, you can delete the token and generate a new one.*

At this point, run:
```shell
hf auth login
```
and paste your access token.

If authentication succeeds, you should see your account when running:
```shell
hf auth whoami
```

> [!TIP]
> For more information about access tokens and the CLI, see:
> - [Access Tokens](https://huggingface.co/docs/hub/en/security-tokens)
> - [CLI](https://huggingface.co/docs/huggingface_hub/en/guides/cli)

## Running the code
After installing the required packages and adding your access token to your machine, interact with the project using:
```shell
python -m main
```

> [!TIP]
> You can run the same command with the `--help` option to list available arguments.

### Using another model
To use a different model, create a new file in the [`models/`](./models/) subfolder and define a function called `prepare_text`. See the example for [Qwen3](./models/qwen3.py).

Next, add an entry to the `MODELS` dictionary in [`utils.py`](utils.py) using the following pattern:
```python
from transformers import AutoModelForCausalLM
from models import your_model

MODELS = {
    "your_model": (
        "checkpoint_name_on_hf",
        AutoModelForCausalLM.from_pretrained,
        your_model.prepare_text,
    )
}
```

If your model requires additional arguments, you can use `functools.partial` to specify them. See the Qwen3 entry for an example.

Finally, run the project and specify the model name:
```shell
python -m main --model-name your_model
```

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This work is licensed under a [MIT License](https://opensource.org/licenses/MIT).