from fastapi import FastAPI
from datetime import date, timedelta
# from pydantic import BaseModel

app = FastAPI()

# class Validate(BaseModel):
#     current_date: date
#     offset: int

# task 4
@app.get('/')
def say_hello():
    return 'hello, world'

# task 5
@app.get('/')
def sum_two(a: int, b: int):
    return a + b

# task 6
@app.get('/sum_date')
def sum_date(current_date: date, offset: int):
    # валидация входных данных
    if isinstance(current_date, date) and isinstance(offset, int):
        return current_date + timedelta(days=offset)

