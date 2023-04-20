import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware

from .schema import *
from .models import *
# loading env
prod = False

if not prod:
    load_dotenv(".env")

app = FastAPI()

# Adding middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    DBSessionMiddleware, 
    db_url=os.environ["DATABASE_URL"]
)

# get all pallete
@app.get("/",tags=['coolor'])
async def getPallete():

    palletes = db.session.query(Pallete).all()
    return palletes[::-1]

# create pallete
@app.post("/create/",tags=['coolor'],response_model=PalleteSchema)
async def createPallete(data: PalleteSchema):
    db_pallete = Pallete(color1=data.color1,color2=data.color2,color3=data.color3,color4=data.color4,color5=data.color5)
    db.session.add(db_pallete)
    db.session.commit()
    return db_pallete


