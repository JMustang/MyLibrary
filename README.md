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

## Create a CRUD

## What CRUD is

- CRUD is an acronym
  for four functions that are used to manipulate data
  in a data storage application.

**C -> CREATE:** create a resource.
**R -> READ:** read a resource.
**U -> UPDATE:** update a resource.
**D -> DELETE:** delete a resource.

## What is a resource?

- The data that an API
  provides or allows us to manipulate.
  This is accessible through an endpoint.

| ENDPOINT        | HTTP METHOD | DESCRIPTION             |
| --------------- | ----------- | ----------------------- |
| /books          | GET         | Get a list of all books |
| /books          | POST        | Create a book           |
| /book/{book_id} | PATCH       | Update a book           |
| /book/{book_id} | DELETE      | Delete a book           |

---

## CRUD

### A basic CRUD structure

```py
from fastapi import FastAPI
import books as db

app = FastAPI()

@app.get('/books')
async def book():
  return db.books

@app.post('/books')
async def book():
  return db.books

@app.patch('/book/{book_id}')
async def book():
  return db.books

@app.delete('/book/{book_id}')
async def book():
  return db.books
```

This is a basic example of a CRUD, I will explain
every line of this code.

---

1.**from fastapi import FastAPI, HTTPException, status**

- **FastAPI:** Here, we are importing the **FastAPI** class from the \* **FastAPI** library. This class is responsible for creating our web application. It provides the tools needed to define routes, manage requests and responses, and much more.

- **HTTPException:** It is used to throw custom HTTP exceptions, such as 404 (not found) error.

- **status:** Makes it easier to use HTTP status codes, making code more readable and less error-prone when using numbers.

  2.**from pydantic import BaseModel**
  We import **BaseModel** from **Pydantic**, which will be used to define the book's data model and validate inputs.

  3.**import books as db**
  We are importing a module called **books** and referencing it as db. We can assume that books is a Python module that contains information about a set of books (probably a fake database for demonstration purposes). This line allows us to use db.books in different routes to access and modify the list of books.

  4.**app = FastAPI()**
  Here, we are creating an instance of the **FastAPI** application. The app variable is our **FastAPI** application and all routes will be registered from it. When you start the server, this instance is the one that accepts and handles requests.

  5.**Book Model Definition**

```py
class Book(BaseModel):
    title: str
    author: str
    published_year: int
    id: int
```

- **class Book(BaseModel)**
  We create a Book class that inherits from BaseModel. This defines the format of the data we expect for each book.

- **title, author, published_year, id**
  Each of the class attributes defines the type of data expected:

- **title** and **author** are strings.
- **published_year** is an integer representing the year of publication.
- **id** is a unique identifier for the book (also an integer).

Now, let's go to the routes:

---

GET **/books**

```py
@app.get('/books', response_model=list[Book])
async def book():
    return db.books
```

**@app.get('/books')**
This is a decorator that defines the /books route. The @app.get decorator means that this function will be called when the client makes an HTTP GET request to the /books path.

**async def book():**
The book function is defined as async, which means that it is asynchronous. **FastAPI** supports asynchronous programming, allowing multiple requests to be handled efficiently without blocking execution. This is especially useful for I/O scenarios, such as database calls.

**return db.books**
The function simply returns db.books. This means that we are sending back to the client the list of books that are defined in the books module. Presumably, db.books is a list of dictionaries, with each dictionary representing a book.
