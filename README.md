# Project Hotel Management


![Hotel Management](https://github.com/neonklr/hotel-management/assets/55053464/9c152b08-1410-4ec5-878e-77eecbfefa42)

![Hotel Management](https://github.com/neonklr/hotel-management/assets/55053464/e5213777-8051-4ce1-9f71-10dd9282c1d5)


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



## Run this project

Note :- if you dont have virtual environment activated and are using `poetry` then add a prefix `poetry run` before the following commands

1. complete setting up project on local environment
2. run `python manage.py migrate`
3. run `python manage.py runserver`

optionally, if you want to create a super user (admin user) to access admin dashboard present at `/admin` then run `python manage.py createsuperuser`


## Running tests for the project

Note :- if you dont have virtual environment activated and are using `poetry` then append `poetry run ` before the following commands

1. run `coverage run --source='.' manage.py test`
2. run `coverage report` to get report of the coverage test we just ran
