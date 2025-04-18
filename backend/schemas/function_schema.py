from pydantic import BaseModel

class FunctionCreate(BaseModel):
    name: str
    language: str
    timeout: int
    code: str

class FunctionUpdate(BaseModel):
    code: str
