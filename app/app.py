from fastapi import FastAPI
from app.api.routes import ROUTES
from app.views import get_admin
def setup_routers(app: FastAPI) -> None:
	for prefix, router in ROUTES.items():
		app.include_router(router, prefix=prefix)

def get_app() -> FastAPI:
	app = FastAPI(
		title = "Rain Messanger",
	)
	setup_routers(app)
	get_admin(app)
	return app