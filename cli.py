# позволет запускать приложение в поределенной конфигурации
from enum import Enum
from typing import Annotated

from typer import Typer, Argument
from app.main import run_api_app

cli = Typer(help = 'Rain messanger CLI')

class Apps(str, Enum):
	api = 'api'
	background_tasks = "background_tasks"

@cli.command(help = "Run Api app")
def run(
	app: Annotated[Apps, Argument(help = "App to run")] = Apps.api
):
	match Apps.api:
		case Apps.api:
			run_api_app()
		case Apps.background_tasks:
			pass

# если python -m cli.py api, то приложение встает как апи
# если python -m cli.py background_tasks, то приложение ничего не делает. Тут будут отложенные задачи. Позволяет масштабирать приложение таким # # образом, чтобы одно приложение поднималось и работало с апи, а второе - с отложенными задачами
# теперь можно поднимать несколько приложений под api, и ещё условно 10 под отложенные задачи(background_tasks)