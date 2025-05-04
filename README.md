# DevContainer Boilerplate for python uv fastapi

## Introduction
Welcome to `devcontainer-boilerplate-python-uv-fastapi`! This repository is designed to provide a quick and easy way to create a enpoint service with fastapi. It includes a development container configuration to streamline the setup process and ensure a consistent environment for python uv development.

## About the Resume Template
The enpoint template used in this boilerplate is creating using python packages [fastapi](https://fastapi.tiangolo.com/) and [typer](https://typer.tiangolo.com/) with [uv](https://docs.astral.sh/uv/) for packaging


## Prerequisites
Before you begin, ensure you have the following installed:
- [Docker](https://www.docker.com/get-started) (for running the development container)
- [Visual Studio Code](https://code.visualstudio.com/) (for local development)
- [Dev - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

## Using the DevContainer in Visual Studio Code
1. **Clone the Repository**: Clone this repository to your local machine.
2. **Open in VS Code**: Open the cloned repository folder in Visual Studio Code.
3. **Reopen in Container**: When prompted, use the Remote-Containers extension to reopen the project inside the development container. Alternatively, you can use the Command Palette (`Ctrl+Shift+P`) and select "Remote-Containers: Reopen in Container".

4. **Edit Code**: Once the container is running, you can start editing your code `sample-service/src/sample_service/base.py`
5. **Build**: Use the uv tools for handle the life cycle of the project.

## Using the DevContainer in GitHub Codespaces
1. **Open the Repository in GitHub**: Navigate to the repository on GitHub.
2. **Start a New Codespace**: Click the "Code" button and then "Open with Codespaces". Follow the prompts to create a new codespace.


## Support and Contributions
If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. Contributions to enhance this boilerplate are always welcome!
