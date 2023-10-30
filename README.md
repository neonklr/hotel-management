# Project Hotel Management

## Setup

You can choose any of the following methods to setup the project.

#### 1. Using poetry

1. Install [poetry](https://python-poetry.org/docs/#installation) using command `pip install poetry`
2. Clone the repository
3. Run `poetry install` to install the dependencies

Optionally, if you are a vscode user, you can add the generated venv path to the environment paths of vscode to ensure auto-activation of the virtual environment.

#### 2. Using pip

1. Clone the repository
2. Run `pip install .` to install the dependencies

_Warning :- doing this directly in your global environment is not recommended. Use a virtual environment instead. This method is intended for those with alternate methods to generate virtual environments other than poetry._

#### 3. using task

_Note :- this requires you to have [taskfile](https://taskfile.dev/) installed on your system._<br>
_Info :- This method internally uses method 1 to setup dev environment._

1. Clone the repository
2. Run `task setup:dev`

#### 4. Using devcontainer

_Note :- this requires you to have [docker](https://www.docker.com/) and [vscode decontainer extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installed on your system._

1. Clone the repository
2. Open the repository in vscode
3. Click on the green button at the bottom left corner of the vscode window
4. Select `Reopen in Container`
5. Wait for the devcontainer to build
6. Run either of method 1, 2 or 3 to install the dependencies (Recommended is method 3)
