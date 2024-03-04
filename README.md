# README

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

## Run flake8

```bash
poetry run flake8 app.py
```
