from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import image_tool 


app = FastAPI(
    title="webXtras API",
    description="API for webXtras",
    version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(image_tool.router , prefix='/image' , tags=['image'])


@app.get("/")
async def root():
    return {"message": "Hello World"}
