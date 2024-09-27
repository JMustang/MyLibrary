# MyLibrary

![library](Library.jpeg)

- A simple app to manage my read progress.

## **Prerequisites**

Have the following installed:

- python>= 3.10
- PostgreSQL
- Redis

## **Project Setup**

1.Create directory:

```bash
mkdir MyLibrary
```

2.Navigate to the project directory:

```bash
cd MyLibrary
```

3.Create and activate a virtual environment:

```bash
# macOS or linuxOS
python3 -m venv env

# activate the virtual environment
source env/bin/activate
```

## **FastAPI**

- I used the **fastapi** framework to create the backend.

## Simple app

- I will create a very simple application to test if everything is OK so far.

  1.In the root directory of your project create a main.py file.

```bash
touch main.py
```

2.Install fastapi dependency:
on your terminal:

```bash
pip install "fastapi[standard]"
```

3.On the main.py file add the following code.

```py
# main.py
from fastapi import # FastAPI imported the FastAPI class from the fastapi package.

app = FastAPI() # create an instance of the FastAPI class named app.

@app.get('/') # The @app decorator associates the function with the HTTP GET method via the get method.
async def read_root(): # creating a function named read_root.
    return {"message": "Hello World!"}
    # Then we will return a simple message. If everything is OK, the message "Hello World!" should appear.
```

4.Run the code with the command:

```bash
fastapi dev main.py
```

- The fastapi dev command enables us to execute our FastAPI application in development mode.

- If everything is OK, it should return this in the terminal:

```bash
INFO     Using path main.py
INFO     Resolved absolute path /home/jod35/Documents/fastapi-beyond-CRUD/main.py
INFO     Searching for package file structure from directories with __init__.py files
INFO     Importing from /home/jod35/Documents/fastapi-beyond-CRUD

 ╭─ Python package file structure ─╮
 │                                 │
 │      🐍 main.py                 │
 │                                 │
 ╰─────────────────────────────────╯

INFO     Importing module main.py
INFO     Found importable FastAPI app

 ╭─ Importable FastAPI app ─╮
 │                          │
 │  from main import app    │
 │                          │
 ╰──────────────────────────╯

INFO     Using import string main:app

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯
```
