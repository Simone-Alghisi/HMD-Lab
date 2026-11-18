<!-- omit from toc -->
# HMD Lab Repository

Official repository for the [Human-Machine Dialogue (HMD)](https://disi.unitn.it/~riccardi/page7/styled-3/page16.html) course at the University of Trento.

> [!CAUTION]
> For any issue, write an email to s.alghisi@unitn.it and include christian.moiola@unitn.it in cc.

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
2. [Project Report Template](https://drive.google.com/file/d/1TjRynDH-Jn8rusjnYTsC73xK9QKRbeyE/view?usp=share_link) (max 4 pages, references and appendix excluded)
3. Live Demo or Video Recordings (showing the system capabilities, such as fallback policy, mixed initiative, and over-/under-informative users)

> [!TIP]
> A video demonstration is strongly recommended as it is more reliable and easier to present.
> 


<!-- omit from toc -->
### Project Submission
Submit all of the required materials no later than 7 days before the exam date to s.alghisi@unitn.it (include christian.moiola@unitn.it in cc).


<!-- omit from toc -->
### Exam Format
During the exam, you will:
- Present your system (live or via video)
- Answer questions about design choices, methods, evaluation, limitations, and improvements
- Demonstrate understanding of the underlying concepts taught in the course


## Getting started
This section guides you through the necessary steps to run the code.


### Azure

As a first step, you need to log in to Azure, claim a virtual machine, and configure your SSH connection.

> ⚠️ **Important:** Each student has a quota of **50 hours** of virtual machine usage.
> Always remember to **stop your virtual machine from the Azure Portal** when you finish working to preserve your usage quota.
> Simply closing the SSH connection or VS Code does not stop the virtual machine.

#### Setup

You should have received an email in your Unitn inbox containing the information required to access your virtual machine.

Follow these steps:

1. Open the [Azure Portal](https://portal.azure.com/).
2. Log in using your **Unitn email credentials**.
3. Search for and open the **DevTest Labs** service.
4. Access the **CorsoHMD-Riccardi-US** lab.
5. Expand the **My Lab** menu and select **Claimable virtual machines**.
6. Select an available virtual machine, click the three-dot menu, and claim the machine.
7. Once claimed, your virtual machine will be available in the **Overview** section of the lab.
8. Select your virtual machine and use the **Start** and **Stop** buttons to manage its power state.

#### Connect via SSH

To connect to your virtual machine:

1. Start your virtual machine from the Azure Portal.
2. Click **Connect with SSH**.
3. In the connection panel, locate the **Connect via password** section and copy the provided SSH command.
4. Replace the `<vm-username>` placeholder with the actual username provided in the email.

   The command should look like this:

   ```bash
   ssh username@ip-address
   ```

5. Open a terminal on your local computer and run the SSH command.
6. When connecting for the first time, confirm that you want to add the host to your list of known hosts by typing `yes`.
7. Enter the password provided in the email.

After your first login, you must change your password by running:

```bash
passwd
```

Follow the instructions in the terminal and securely store your new password for future use.

> **Note:** You have administrator privileges (`sudo`) on your virtual machine.
> Currently, only the NVIDIA drivers are preinstalled. You will need to install any additional software and dependencies required for the lab activities.

#### VS Code (Optional)

You can also connect to your virtual machine directly from Visual Studio Code (VS Code) using the **Remote - SSH** extension.

1. Open VS Code.
2. Install the **Remote - SSH** extension from Microsoft.
3. Open the Command Palette (`Ctrl+Shift+P` on Windows/Linux or `Cmd+Shift+P` on macOS).
4. Select **Remote-SSH: Connect to Host...**.
5. Select **Add New SSH Host...**.
6. Paste your SSH command, making sure it contains the correct username and IP address.
7. Select the default SSH configuration file to save the connection.
8. Open the Command Palette again and select **Remote-SSH: Connect to Host...**.
9. Select your newly configured host and enter your password when prompted.

> 💡 Once VS Code has been configured, you only need to start your virtual machine from the Azure Portal and select the saved SSH host to reconnect.

### Clone the Repository

Once connected to your virtual machine, open a terminal and clone this repository by running:

```bash
git clone https://github.com/Simone-Alghisi/HMD-Lab.git
```

### Installation

> [!IMPORTANT]
> Ensure that you have Miniconda [conda](https://www.anaconda.com/docs/getting-started/miniconda/install#linux-2) installed before proceeding.

Create a Python environment using the following command:
```shell
conda create -n hmd python=3.11
```

In the repository folder, activate the environment and install the required packages:
```shell
conda activate hmd
pip install -r requirements.txt
```

After installing all the required packages, remove any remaining pip and Conda package caches:

```shell
pip cache purge
conda clean --all -y
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
  3. If the problem persists, send an email to alessandro.tomasi@unitn.it (put s.alghisi@unitn.it and christian.moiola@unitn.it in CC)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This work is licensed under a [MIT License](https://opensource.org/licenses/MIT).