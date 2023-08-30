from fastapi import FastAPI

from api import api_router
from events import startup_event

def get_application():
    app = FastAPI()
    app.include_router(api_router)

    app.add_event_handler(
        "startup",
        startup_event,
    )

    # application.add_event_handler(
    #     "shutdown",
    #     close_db_connection,
    # )

    return app


app = get_application()
