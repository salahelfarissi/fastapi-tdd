"""Main application and routing logic."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import ping, summaries
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    """Create a FastAPI application with all the routing logic."""
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )

    return application


app = create_application()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager."""
    log.info("Starting up...")
    init_db(app)
    log.info("Startup complete!")
    try:
        yield
    finally:
        log.info("Shutting down...")
        log.info("Shutdown complete!")
