from fastapi import FastAPI
from backend.api.routes import router
from backend.db.database import init_db

app = FastAPI(title="Lambda Serverless")

init_db()
app.include_router(router)
