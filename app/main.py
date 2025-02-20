from fastapi import FastAPI
from app.startup import startup
from app.api import api_router

app = FastAPI(
    title="Gym Management API - DEOLANG",
    summary="This is the documentation of Gym Management API developed by Deolang. It is a JSON based RESTful API with custom endpoints to streamline gym management.",
    on_startup=[startup],
    contact={
        "name": "Email- Uday Subba",
        "email": "udaysubba2004@gmail.com",
    },
    servers=[
        {"url": "/api", "description": "Default api URL Route"},
    ],
    root_path="/api",
)

@app.get("/",
    name= "Api Status",
    description= """
        Root route to check the status of the Backend.
            """,
    tags=["Root"]
         )
async def root():
    return {"status":"true", "message": "Api server is up and running"}

app.include_router(api_router.router)