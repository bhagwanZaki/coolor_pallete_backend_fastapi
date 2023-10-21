import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware

from .schema import *
from .models import *
# loading env
prod = True
DATA_LIMIT = 12

if not prod:
    load_dotenv(".env",override=True)

app = FastAPI()

# Adding middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
print(os.environ["DATABASE_URL"])
app.add_middleware(
    DBSessionMiddleware, 
    db_url=os.environ["DATABASE_URL"]
)

# get all pallete
@app.get("/",tags=['coolor'])
async def getPallete(page : int):
    palletes = db.session.query(Pallete).order_by(Pallete.id.desc()).offset((page - 1) * DATA_LIMIT).limit(DATA_LIMIT).all()
    print(len(palletes))     
    return {"data": palletes,"isLast": len(palletes) < DATA_LIMIT}

# create pallete
@app.post("/create/",tags=['coolor'],response_model=PalleteSchema)
async def createPallete(data: PalleteSchema):
    db_pallete = Pallete(color1=data.color1,color2=data.color2,color3=data.color3,color4=data.color4,color5=data.color5)
    db.session.add(db_pallete)
    db.session.commit()
    return db_pallete


