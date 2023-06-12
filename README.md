https://fastapi-langchain.vercel.app/


# fastapi-template

A FastAPI template with local development environment

## Setup dev environment:

### Setup virtualenv environment:
```
virtualenv -p python3.10 env
```

### Activate environment
```
source env/bin/activate
```

### Inatall the following libraries:
```
pip install "fastapi[all]" uvicorn openai langchain pypdf  chromadb tiktoken
```

### If you would like to shut down the environment:
```
deactivate
```

---

## Run local dev environment

### If the enviromment is not running, activate environment:
```
source env/bin/activate
```

## Run application

```
python -m uvicorn app.main:app --reload
```

### API access:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Swager accees:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Stop local server
```
ctrl + c
```

### Shut down environment:
```
deactivate
```

---

## Vercel deployment

Add a vercel.json file to the root of the project:

```
{
  "builds": [
    {
      "src": "app/main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app/main.py"
    }
  ]
}
```

Include requirements.txt file in the root of the project
```
pip freeze --local > requirements.txt
```


Add to Vercel environment variables:
```
PORT 8000
```
