from fastapi import FastAPI, HTTPException

from fast_zero.shemas import Message, UserSchema, UserPublic, UserDb
from http import HTTPStatus

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return Message(message='Hello world!')


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_users(user: UserSchema):
    user_with_id = UserDb(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK)
def read_users():
    return {'users': database}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDb(**user.model_dump(), id=user_id)

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='User or id not found!'
        )
    database[user_id - 1] = user_with_id

    return user_with_id
