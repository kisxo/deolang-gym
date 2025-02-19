from fastapi import FastAPI
from app.startup import startup

app = FastAPI(
    title="Gym Management API - DEOLANG",
    summary="This is the documentation of Gym Management API developed by Deolang. It is a JSON based RESTful API with custom endpoints to streamline gym management.",
    on_startup=[startup],
    contact={
        "name": "Email- Uday Subba",
        "email": "udaysubba2004@gmail.com",
    },
    servers=[
        {"url": "/api/v1", "description": "Default api URL Route"},
    ],
    root_path="/api/v1",
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