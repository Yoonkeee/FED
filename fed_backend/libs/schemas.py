from pydantic import BaseModel


class JobPostBase(BaseModel):
    # post_id: int
    # start_date: str
    # end_date: str
    # company_id: int
    # company_name: str
    # career: int
    # tech_stacks: str
    # team_id: int
    # team_name: str
    # post_link: str
    # address: str
    pass


class GetListByStack(JobPostBase):

    class Config:
        orm_mode = True
