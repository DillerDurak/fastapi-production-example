'''
    Main
'''

from fastapi import FastAPI
from pydantic import BaseModel

from .settings import settings

app = FastAPI(title="Production-Ready project")


class Status(BaseModel):
    ''' Status class '''
    status: int=200


@app.get(settings.main_url, response_model=Status)
async def get_status():
    ''' Status endpoint '''
    return Status(status=202)
