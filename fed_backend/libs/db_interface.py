import pymysql
import environ
import os
from pathlib import Path
from typing import *
from libs import cleanser
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Interface:
    cleansed_data: dict = {}
    cursor: pymysql.Connection.cursor = None
    db: pymysql.connections.Connection = None
    setter: pymysql.Connection.cursor = None
    getter: pymysql.Connection.cursor = None
    column_names: List[str] = ''

    # sqlalchemy_db_url: str = ''
    # engine: sqlalchemy.engine.base.Engine = None
    # session: sqlalchemy.orm.session.Session = None
    # base: sqlalchemy.ext.declarative = None


    # db = pymysql.connect( host=HOST, port=PORT, db=SCHEMA, user=USER, passwd=PASSWORD, charset="utf8", )
    def __init__(self):
        # database connection
        env = environ.Env()
        BASE_DIR = Path(__file__).resolve().parent.parent
        environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
        HOST, PORT, SCHEMA, DB_USER, PASSWORD = env("HOST"), int(env("PORT")), env("SCHEMA"), env("DB_USER"), env("PASSWORD")
        self.db = pymysql.connect(host=HOST, port=PORT, user=DB_USER, password=PASSWORD, db=SCHEMA, charset="utf8")
        self.setter = self.db.cursor()
        self.getter = self.db.cursor()
        self.getter.execute("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_NAME`='job_post'")
        self.column_names = [item[0] for item in self.getter.fetchall()]
    # just check only if post_id exists in job_post table

    def duplication_check(self):
        select_query = f"""
        SELECT post_id FROM job_post WHERE post_id = {str(self.cleansed_data['post_id'])}
        """
        self.getter.execute(select_query)
        if self.getter.fetchone():
            return True
        return False

    def set(self, cleansed_data: dict):
        # input data to job_post table
        self.cleansed_data = cleansed_data
        if not self.duplication_check():
            insert_query = f"""
            INSERT INTO job_post VALUES (
            {str(self.cleansed_data['post_id'])}, 
            '{self.cleansed_data['start_date']}', 
            '{self.cleansed_data['end_date']}', 
            {str(self.cleansed_data['company_id'])}, 
            '{self.cleansed_data['company_name']}', 
            {str(self.cleansed_data['career'])}, 
            '{', '.join(str(key) for key in self.cleansed_data['tech_stacks'])}', 
            {str(self.cleansed_data['team_id'])}, 
            '{self.cleansed_data['team_name']}', 
            '{self.cleansed_data['post_link']}', 
            '{self.cleansed_data['address']}',
            '{self.cleansed_data['company_logo_url']}'
            )
            """
            # {str(self.cleansed_data['tech_stacks'].keys())},
            # print(insert_query)

            self.setter.execute(insert_query)
            self.db.commit()
        # else:
        #     insert_query = f"""
        #     UPDATE job_post
        #     SET COMPANY_LOGO_URL =
        #     '{self.cleansed_data['company_logo_url']}'
        #     WHERE POST_ID = {str(self.cleansed_data['post_id'])}
        #     """
        #     self.setter.execute(insert_query)
        #     self.db.commit()

    def get_by_company_name(self, comany_name: str):
        select_query = f"""
        SELECT * FROM job_post WHERE COMPANY_NAME = '{comany_name}' 
        """

        self.getter.execute(select_query)
        selected = self.getter.fetchall()

        result = [{key: val for key, val in zip(self.column_names, item)} for item in selected]
        return result

    def get_list_by_stacks(self, tech_stacks: str):
        condition: str = ''
        result:  List[str] | List[dict] | str = []
        for tech_stack in tech_stacks.split(','):
            result.append(f"TECH_STACKS LIKE '%{tech_stack}%'")
        condition = ' AND '.join(result)
        select_query = f"""
        SELECT * 
        FROM job_post 
        WHERE 
        {condition}
        """
        self.getter.execute(select_query)
        selected = self.getter.fetchall()
        result = [{key: val for key, val in zip(self.column_names, item)} for item in selected]
        return result

    def get_list_all(self):
        pass

