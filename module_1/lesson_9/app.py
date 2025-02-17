from fastapi import FastAPI, HTTPException, Depends
from datetime import date, timedelta
from pydantic import BaseModel
from db_con import connection
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# task 7
class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: date
    class Config:
        orm_mode = True

class PostResponse(BaseModel):
    id: int
    text: str
    topic: str
    class Config:
        orm_mode = True

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

# task 8
@app.post('/user/validate')
def user_validate(user: User):
    return f"Will add user: {user.name} {user.surname} with age {user.age}"


# task 9 and 10
def get_db():
    conn = psycopg2.connect(
        connection, 
        cursor_factory=RealDictCursor  # курсор возвращает dict
    )
    return conn
  
@app.get('/user/{id}')
def user_info(id: int, db=Depends(get_db)):
    with db.cursor() as cursor:
        sql_query = f'''
            select
                gender
                , age
                , city
            from "user"
            where id = {id}
        '''
        cursor.execute(sql_query)
        result = cursor.fetchone()
        if result is None:
            raise HTTPException(404, detail='user not found')
        else:
            return result


# task 11
@app.get('/post/{id}', response_model=PostResponse)
def post_id(id: int, db=Depends(get_db)) -> PostResponse:
    with db.cursor() as cursor:
        sql_query = f'''
            select
                id
                , text
                , topic
            from post
            where id = {id}
        '''
        cursor.execute(sql_query)
        result = cursor.fetchone()
        if result is None:
            raise HTTPException(404, detail='not found')
        else:
            return result
