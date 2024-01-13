import logging

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api import ping
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)
    log.info("Startup complete!")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
    log.info("Shutdown complete!")