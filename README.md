# README

## only for Docker remote container

sync poetry.lock and pyproject.toml under .devcontainer

```bash
cp poetry.lock ./devcontainer
cp pyproject.toml ./devcontainer
```

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
