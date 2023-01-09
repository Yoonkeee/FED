from fastapi import FastAPI
from libs import parser, cleanser, id_generator, db_interface
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/get/list/')
async def get_list(tech_stacks: str):
    print(tech_stacks)
    return db_interface.Interface().get_list(tech_stacks)


@app.get('/get/list/all')
async def get_list_all():
    return db_interface.Interface().get_list_all()


# set router
@app.get("/get/{company_name}")
def get_data(company_name: str):
    return db_interface.Interface().get(company_name)

