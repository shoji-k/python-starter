# README

### in terminal

run `bash` to boot bash

## Docker container

build

```bash
docker build -f ./.devcontainer/Dockerfile -t python-sandbox:latest .
```

Connect to the container

```bash
docker run -it --rm -v "$(pwd):/app" python-sandbox:latest bash
```

## Python package

```bash
poetry add (package)
```

## Run Python script

```bash
poetry run python app.py
```

## Run flake8

```bash
poetry run flake8 app.py
```

## be in venv

```bash
poetry shell
```

so you don't need to type `poetry run` everytime
