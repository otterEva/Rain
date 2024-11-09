from fastapi import FastAPI
from app.api.MiscRouters import router as router_health
from app.api.AuthUserRouters import router as register_router
import uvicorn

app = FastAPI()
app.include_router(router_health)
app.include_router(register_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
