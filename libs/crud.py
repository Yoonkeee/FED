from sqlalchemy.orm import Session
from libs import models, schemas


def get_job_post(db: Session, post_id: int):
    return db.query(models.JobPost).filter(models.JobPost.post_id == post_id).first()


def get_post_by_stacks(db: Session, tech_stacks: str, limit: int = 100):

    # filtered_query by tech_stacks
    # filtered_query = db.query(models.JobPost).filter(models.JobPost.tech_stacks.like(f'%{tech_stacks}%'))

    filtered_query = db.query(models.JobPost).filter(
        models.JobPost.tech_stacks.like('%cpp%'))
    return filtered_query.limit(limit).all()
    # print(filtered_query.all())
    # return filtered_query.all()
