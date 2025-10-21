from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from aula01.schemas import Message  

app = FastAPI()


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