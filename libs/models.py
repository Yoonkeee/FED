from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from libs.database import Base
# import schemas
# import crud
# import database


class JobPost(Base):
    __tablename__ = "job_post"
    __table_args__ = {'extend_existing': True}
    post_id = Column(Integer, primary_key=True)
    start_date = Column(String)
    end_date = Column(String)
    company_id = Column(Integer)
    company_name = Column(String)
    career = Column(Integer)
    tech_stacks = Column(String)
    team_id = Column(Integer)
    team_name = Column(String)
    post_link = Column(String)
    address = Column(String)

    # items = relationship("Item", back_populates="job_post")


# columns = JobPost.__table__.columns
# print(columns)
# for column in columns:
#     print(column.name)

