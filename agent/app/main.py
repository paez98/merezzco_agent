from agent.app.routes.agent_route import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)


@app.get("/home")
def home():
    return {"hello": "world"}
