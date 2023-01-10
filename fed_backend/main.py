import requests
from typing import *
from libs import parser, cleanser, id_generator, \
    db_interface, crud, models, schemas
from libs.database import SessionLocal, engine
from fastapi import FastAPI, Depends, HTTPException

# models.Base.metadata.create_all(bind=engine)
# from sqlalchemy.orm import Session

app = FastAPI()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/get/list/')
async def get_list_by_stacks(tech_stacks: str):
    print(tech_stacks)
    return db_interface.Interface().get_list_by_stacks(tech_stacks)


@app.get('/get/list/all')
async def get_list_all():
    return db_interface.Interface().get_list_all()


# set router
@app.get("/get/{company_name}")
def get_by_company_name(company_name: str):
    return db_interface.Interface().get_by_company_name(company_name)


# @app.get('/get2/', response_model=schemas.GetListByStack)
# async def get2(tech_stacks: str, db: Session = Depends(get_db)):
#     print(tech_stacks)
#     result = crud.get_post_by_stacks(db, tech_stacks=tech_stacks)
#     # for item in result:
#     #     print(item.__dict__)
#     print({'result': [item.__dict__ for item in result]})
#     return {'result': [item.__dict__ for item in result]}
