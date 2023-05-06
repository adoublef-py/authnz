# Authnz

This repository follows best practises when building an authentication service in the Python language.

## How to run locally

The pre-requirements to setup this project locally:

- Docker is assumed to be already installed on your device. If not you can follow [here](https://docs.docker.com/engine/install/) for installation assistance.

It is advised to run in a [virtual environment](https://docs.python.org/3/library/venv.html) as this common practice amongst python applications. 

A module called [testcontainers](https://github.com/testcontainers/testcontainers-python) will create a sandbox for all dependencies.

```bash
# run application using the local environment.
$ python -m uvicorn app:local --port $"PORT"
```

## Remote application

There are few projects in which this service is being used listed below:

|project|website|
|:---|:---|
|[adoublef/soundcloud](#)|tbc|
