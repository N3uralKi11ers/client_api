from fastapi import APIRouter

from .routes import history_router, terminal_router, cashback_router, mir_router

router = APIRouter()
router.include_router(history_router, tags=["history"], prefix="/history")
router.include_router(cashback_router, tags=["cashback"], prefix="/cashback")
router.include_router(mir_router, tags=["MIR cards"], prefix="/mir")
router.include_router(terminal_router, tags=["terminal"], prefix="/terminal")