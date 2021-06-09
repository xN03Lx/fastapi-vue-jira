# backend without docker

# Project setup

## Requirements

    python > 3.5
    mongodb > 3

## Preparing the environment

Create your python environment

```bash
python3 -m venv env
source env/bin/activate
```

## install dependencies

`pip install -r requirements.txt`

## Configure your .env file

```bash
cp .env.example .env
```

```
MONGO_HOST=
MONGO_USERNAME=
MONGO_PASSWORD=
MONGO_PORT=
MONGO_DB=

JIRA_HOST=
JIRA_USERNAME=
JIRA_API_TOKEN=
```

## Run server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```
