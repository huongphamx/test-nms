from sqlalchemy import ARRAY, BigInteger, ForeignKey, String
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base_model import Base


class Product(Base):
    __tablename__ = "product"

    product_base_id: Mapped[str] = mapped_column(primary_key=True)
    shop_base_id: Mapped[str]
    platform_id: Mapped[int]
    name: Mapped[str]
    price: Mapped[int]
    price_before_discount: Mapped[int | None]
    rating_count: Mapped[int]
    rating_avg: Mapped[float]
    comment_count: Mapped[int]
    like_count: Mapped[int]
    description: Mapped[str]
    url_thumbnail: Mapped[str]
    url_images: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String)))
    historical_sold: Mapped[int]


class ProductPriceHistory(Base):
    __tablename__ = "product_price_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_base_id: Mapped[str] = mapped_column(ForeignKey("product.product_base_id"))
    price: Mapped[int]
    price_ts: Mapped[int] = mapped_column(BigInteger())


class ProductReview(Base):
    __tablename__ = "product_review"

    review_base_id: Mapped[str] = mapped_column(primary_key=True)
    product_base_id: Mapped[str] = mapped_column(ForeignKey("product.product_base_id"))
    platform_id: Mapped[int]
    title: Mapped[str | None]
    content: Mapped[str]
    rating: Mapped[int]
    images: Mapped[list[str]] = mapped_column(
        MutableList.as_mutable(ARRAY(String)), nullable=True
    )
    created_at_platform: Mapped[int] = mapped_column(BigInteger())
    user_username: Mapped[str]
    user_url_image: Mapped[str]


class ProductPriceInsight(Base):
    __tablename__ = "product_price_insight"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_base_id: Mapped[str] = mapped_column(ForeignKey("product.product_base_id"))
    classify_price: Mapped[str | None]
    current_price: Mapped[int]
    ratio: Mapped[int]
    max_price: Mapped[int]
    min_price: Mapped[int]
    delta_price: Mapped[int | None]
