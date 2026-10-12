from pydantic import BaseModel,ConfigDict

class MemoCreate(BaseModel):
    title:str
    content:str

class MemoUpdate(BaseModel):
    title:str | None = None 
    content:str | None = None 

class MemoRead(MemoCreate):
    id:int
    model_config = ConfigDict(from_attributes=True)