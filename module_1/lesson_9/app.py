from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def say_hello():
    return 'hello, world'

@app.get('/')
def sum_two(a: int, b: int):
    return a + b

