from fastapi import APIRouter

from .routes import history_router, terminal_router

router = APIRouter()
router.include_router(history_router, tags=["history"], prefix="/history")
router.include_router(terminal_router, tags=["terminal"], prefix="/terminal")