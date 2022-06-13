from fastapi import APIRouter

from .endpoints.root import router as root_router
from .endpoints.predicthouseprice import router as predicthouseprice_router


router = APIRouter()
router.include_router(root_router)
router.include_router(predicthouseprice_router)