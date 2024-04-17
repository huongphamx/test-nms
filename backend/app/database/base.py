# Import all the models, so that Alembic can read from memory
# and auto generate migration
# https://stackoverflow.com/questions/15660676/alembic-autogenerate-producing-empty-migration
from app.database.base_model import Base  # noqa:F401
from app.product.models import (  # noqa:F401
    Product,
    ProductPriceHistory,
    ProductPriceInsight,
    ProductReview,
)
