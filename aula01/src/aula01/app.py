from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from src.aula01.schemas import Message, User, UserDB, Userlist, UserPublic

app = FastAPI(title='estudos FastAPI - Eduardo Mendes', version='1.0.0')
database = []


@app.get('/', response_model=Message)
def read_root():
    return {'message': 'Hello world'}


@app.get('/html', response_class=HTMLResponse)
def read_html():
    return """
    <html>
        <head>
            <title>Retorna HTML </title>
        </head>
        <body>
            <h1>This is a sample HTML response</h1>
        </body>
    </html>     """


@app.post('/echo', response_model=Message)
def echo_message(msg: Message):
    return {'message': msg.message}


@app.post('/users/', response_model=UserPublic, status_code=201)
def create_user(user: User):
    user_db_id = UserDB(
        username=user.username,
        email=user.email,
        password=user.password,
        id=len(database) + 1,
    )
    return user_db_id


@app.get('/users/', response_model=Userlist)
def list_users():
    return {'users': database}
