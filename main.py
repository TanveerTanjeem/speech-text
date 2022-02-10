from re import L
from unittest import result
import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from tts import tts
import stt
app = FastAPI()

templates = Jinja2Templates(directory="templates")
#app.mount("/static", StaticFiles(directory="static"), name="static")

"""
@app.get('/')
def hello_world():
    return { 'message':'hello' }


@app.get('/')
def index_get(request:Request):
    return templates.TemplateResponse('index.html', context = {'request': request})
"""
@app.get('/')
def form_post(request: Request):
    result = 'Some random sentences ...'
    
    return templates.TemplateResponse('item.html' , context={'request': request, 'result': result})

@app.post('/')
def form_post(request: Request, num: str = Form(...)):
    tts(num)
    #result = stt.workaround()

    
    return templates.TemplateResponse('item.html', context={'request': request, 'num': num,'result': result})
@app.get('/stt')
def form_post(request: Request):
    result = 'Some random sentences ...'
    
    return templates.TemplateResponse('index.html' , context={'request': request, 'result': result})

@app.post('/stt')
def form_post(request: Request):
    #tts(num)
    result = stt.workaround()
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})

#if __name__ == '__main__':
#    uvicorn.run(app)

