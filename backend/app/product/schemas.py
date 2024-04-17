from pydantic import BaseModel, ConfigDict


class ProductRead(BaseModel):
    product_base_id: str
    shop_base_id: str
    platform_id: int
    name: str
    price: int
    price_before_discount: int | None = None
    rating_count: int
    rating_avg: float
    comment_count: int
    like_count: int
    description: str
    url_thumbnail: str
    url_images: list[str]
    historical_sold: int

    model_config = ConfigDict(from_attributes=True)


class ProductPriceInsightRead(BaseModel):
    product_base_id: str
    classify_price: str
    current_price: int
    ratio: int
    max_price: int
    min_price: int
    delta_price: int | None = None

    model_config = ConfigDict(from_attributes=True)


class ProductReviewRead(BaseModel):
    review_base_id: str
    product_base_id: str
    platform_id: int
    title: str | None = None
    content: str
    rating: int
    images: list[str] | None = None
    created_at_platform: int
    user_username: str
    user_url_image: str

    model_config = ConfigDict(from_attributes=True)
