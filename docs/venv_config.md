[AG/2025/01 Linear Drive Control](../README.md)
===

# [virtual environment configuration](/docs/venv_config.md)

## Use python virtual environment

- Create: ```python -m venv venv```
- Activate: ```.\venv\Scripts\activate```
- Deactivate: ```deactivate```

## Install python dependecies in virtual environment

_*A jogosultságkezelések miatt sudo-val kell futtatni a függőségek telepítését!_

- Freeze requirements: ```pip freeze > requirements.txt```
- Install requirements: ```pip install -r requirements.txt```