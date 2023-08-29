from fastapi import FastAPI
import uvicorn

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


if __name__ == '__main__':
    app = get_application()
    uvicorn.run(app, host="localhost", port=3000)