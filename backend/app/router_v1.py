from fastapi import APIRouter

from app.category.router import router as category_router
from app.product.router import router as product_router

router = APIRouter()


router.include_router(category_router, prefix="/categories", tags=["categories"])
router.include_router(product_router, prefix="/products", tags=["products"])
