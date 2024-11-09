from fastapi import FastAPI
from app.api.MiscRouters import router as router_health
from app.api.AuthUserRouters import register_router, login_router, logout_router
import uvicorn

app = FastAPI()

app.include_router(router_health)

app.include_router(register_router)
app.include_router(login_router)
app.include_router(logout_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
