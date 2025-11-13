<!-- omit from toc -->
# HMD Lab Repository

Official repository for the [Human-Machine Dialogue (HMD)](https://disi.unitn.it/~riccardi/page7/styled-3/page16.html) course at the University of Trento.

> [!CAUTION]
> For any issue, write an email to s.alghisi@unitn.it and include mahed.mousavi@unitn.it in cc.

- [Exam](#exam)
- [Getting started](#getting-started)
  - [Azure](#azure)
    - [Setup](#setup)
    - [Log in](#log-in)
    - [VSCode (optional)](#vscode-optional)
  - [Clone the Repo](#clone-the-repo)
  - [Installation](#installation)
  - [Create Hugging Face access token](#create-hugging-face-access-token)
- [Running the code](#running-the-code)
  - [Using another model](#using-another-model)
- [FAQ](#faq)
- [License](#license)


## Exam
This course is project-based only. Your final assessment is entirely determined by the quality of your project and the associated exam discussion. Please read the following guidelines carefully.

> [!CAUTION]
> You must:
> - register on Esse3
> - submit your exam with all the required material
> 
> **no later than 7 days** before the exam date. No extensions allowed.


<!-- omit from toc -->
### Project Overview
Your project must focus on the design, implementation, and evaluation of a conversational system. This includes:
- System Design: Architecture, components, motivation, intended users.
- Implementation: Prompts and additional/external data (e.g., databases or API)
- Evaluation: Evaluation data, automatic and human evaluation, and error analysis.

Please, refer to the link below for the complete project structure.


<!-- omit from toc -->
### Required Deliverables

To be admitted to the exam, you must submit all materials listed below no later than 7 days before the exam date:

1. Code Repository (on Github or Google Drive)
2. [Project Report]((https://docs.google.com/document/d/1WMZdjussMGK2BatA4sA50h3GhmxR3a8usREyfJmST5I/edit?usp=sharing)) (max 4 pages, references and appendix excluded)
3. Live Demo or Video Recordings (showing the system capabilities, such as fallback policy, mixed initiative, and over-/under-informative users)

> [!TIP]
> A video demonstration is strongly recommended as it is more reliable and easier to present.
> 


<!-- omit from toc -->
### Project Submission
Submit all of the required materials no later than 7 days before the exam date to s.alghisi@unitn.it (include mahed.mousavi@unitn.it in cc).


<!-- omit from toc -->
### Exam Format
During the exam, you will:
- Present your system (live or via video)
- Answer questions about design choices, methods, evaluation, limitations, and improvements
- Demonstrate understanding of the underlying concepts taught in the course


## Getting started
This section guides you through the necessary steps to run the code.
### Azure
As a first step, you need to register with Azure and log in to your virtual machine.

> [!CAUTION]
> Remember to **turn off** your virtual machine on Azure every time you finish using it to avoid unnecessary resource usage.

#### Setup
You should have received an email on your Unitn account. Open it and follow the steps below:
1. Click on the **"Register for the lab"** button.
2. Log in using your **Unitn email** credentials.
3. On the Azure Lab Services page, click the **slider** to turn on your virtual machine.
4. Click the **monitor icon** on the right of the slider, set a **password**, and **save it** for later use.

#### Log in
You can access your machine by logging in to [Azure Lab Services](https://labs.azure.com) using your Unitn account, then:

1. Click the **slider** to power on your machine.
2. Click the **monitor icon** on the right of the slider and copy the provided **SSH command**.
3. Open a terminal, paste the command, confirm adding the host to your known list, and log in using the password you set earlier.

#### VSCode (optional)
You can also log in directly from Visual Studio Code (VSCode) using the following procedure:

1. From the main menu, click **"Connect to..."**
2. In the dropdown menu, select **"Connect to Host..."**
3. Choose **"Add New SSH Host..."**
4. Paste the SSH command.
5. Add it to the default SSH configuration.
6. Repeat steps 1 and 2, then connect to the new host using the password saved earlier.

### Clone the Repo
You can clone this repository by running the following command:
```bash
git clone https://github.com/Simone-Alghisi/HMD-Lab.git
```

### Installation

> [!IMPORTANT]
> Ensure that you have [conda](https://www.anaconda.com/docs/getting-started/miniconda/install#linux-2) installed before proceeding.

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

## FAQ
- *Can I use my own resources/external services (e.g., Groq, Ollama, llama.cpp) for the project?* Yes, you can also use them if you want. Consider the fact that we will offer support only for Azure.
- *I cannot connect to Azure, what should I do?* Check the list below
  1. Turn off the VPN (i.e., Global Protect)
  2. Reset the password and try connecting again
  3. If the problem persists, send an email to alessandro.tomasi@unitn.it (put s.alghisi@unitn.it in CC)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This work is licensed under a [MIT License](https://opensource.org/licenses/MIT).