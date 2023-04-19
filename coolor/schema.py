from pydantic import BaseModel, Field

class PalleteSchema(BaseModel):
    color1:str = None
    color2:str = None
    color3:str= None
    color4:str= None
    color5:str= None

    class Config:
        orm_mode = True