# fastapi-template

A FastAPI template with local development environment

### Uses the following libraries:
[FastAPI](https://fastapi.tiangolo.com/)<br>
[uvicorn](https://www.uvicorn.org/)

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
pip install "fastapi[all]" uvicorn
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
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

### API access:

[http://0.0.0.0:8080/](http://0.0.0.0:8080/)

### Swager accees:

[http://0.0.0.0:8080//\docs](http://0.0.0.0:8080/docs)

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
