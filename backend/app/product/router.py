from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select

from app.database.session import AsyncSession, get_async_db

from .models import Product, ProductPriceHistory, ProductPriceInsight, ProductReview
from .schemas import ProductPriceInsightRead, ProductRead, ProductReviewRead

router = APIRouter()


@router.get("/{product_base_id}")
async def get_product_detail(
    *, db: AsyncSession = Depends(get_async_db), product_base_id: str
):
    product_db = await db.scalar(
        select(Product).where(Product.product_base_id == product_base_id)
    )
    if product_db is None:
        raise HTTPException(404, "Product not found")
    product_insight_db = await db.scalar(
        select(ProductPriceInsight).where(
            ProductPriceInsight.product_base_id == product_base_id
        )
    )
    return {
        **ProductRead.model_validate(product_db).model_dump(),
        "price_insight": ProductPriceInsightRead.model_validate(
            product_insight_db
        ).model_dump(),
    }


@router.get("/{product_base_id}/price-history")
async def get_product_price_history(
    *, db: AsyncSession = Depends(get_async_db), product_base_id: str
):
    price_history_list_db = (
        await db.scalars(
            select(ProductPriceHistory).where(
                ProductPriceHistory.product_base_id == product_base_id
            )
        )
    ).all()

    return {
        "price": [price.price for price in price_history_list_db],
        "price_ts": [price.price_ts for price in price_history_list_db],
    }


@router.get("/{product_base_id}/reviews")
async def get_product_reviews(
    *, db: AsyncSession = Depends(get_async_db), product_base_id: str
):
    review_list_db = (
        await db.scalars(
            select(ProductReview).where(
                ProductReview.product_base_id == product_base_id
            )
        )
    ).all()

    return [
        ProductReviewRead.model_validate(review).model_dump()
        for review in review_list_db
    ]
