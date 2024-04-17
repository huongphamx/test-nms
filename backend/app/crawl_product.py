import asyncio
import logging

import httpx
from sqlalchemy import select

from app.database.session import async_session
from app.product.models import (
    Product,
    ProductPriceHistory,
    ProductPriceInsight,
    ProductReview,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def crawl_products():
    product_base_ids = [
        "1__5382617241__227642622",
        "1__7370776212__299794970",
        "1__13848730793__545226246",
        "1__13951953339__253482297",
        "1__9943772020__291306617",
        "1__13548704707__545226246",
    ]
    async with async_session() as db:
        for id in product_base_ids:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"https://apiv3.beecost.vn/product/detail?product_base_id={id}&type=new"
                )
                if response.status_code == 200:
                    product_data = response.json()["data"]["product_base"]
                    product_db = await db.scalar(
                        select(Product).where(
                            Product.product_base_id == product_data["product_base_id"]
                        )
                    )
                    if product_db is None:
                        product_obj = Product(
                            product_base_id=product_data["product_base_id"],
                            shop_base_id=product_data["shop_base_id"],
                            platform_id=product_data["platform_id"],
                            name=product_data["name"],
                            price=product_data["price"],
                            price_before_discount=product_data["price_before_discount"],
                            rating_count=product_data["rating_count"],
                            rating_avg=product_data["rating_avg"],
                            comment_count=product_data["comment_count"],
                            like_count=product_data["like_count"],
                            description=product_data["description"],
                            url_thumbnail=product_data["url_thumbnail"],
                            url_images=product_data["url_images"],
                            historical_sold=product_data["historical_sold"],
                        )
                        db.add(product_obj)

        await db.commit()


async def crawl_product_price_history():
    product_base_ids = [
        "1__5382617241__227642622",
        "1__7370776212__299794970",
        "1__13848730793__545226246",
        "1__13951953339__253482297",
        "1__9943772020__291306617",
        "1__13548704707__545226246",
    ]
    async with async_session() as db:
        for id in product_base_ids:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"https://apiv3.beecost.vn/product/history_price?product_base_id={id}"
                )
                if response.status_code == 200:
                    price_data = response.json()["data"]["product_history_data"][
                        "item_history"
                    ]["price"]
                    price_ts_data = response.json()["data"]["product_history_data"][
                        "item_history"
                    ]["price_ts"]
                    for price, price_ts in zip(price_data, price_ts_data):
                        product_price_history_db = await db.scalar(
                            select(ProductPriceHistory).where(
                                ProductPriceHistory.price == price,
                                ProductPriceHistory.price_ts == price_ts,
                            )
                        )
                        if product_price_history_db is None:
                            product_price_history_obj = ProductPriceHistory(
                                product_base_id=id,
                                price=price,
                                price_ts=price_ts,
                            )
                            db.add(product_price_history_obj)

        await db.commit()


async def crawl_product_review():
    product_base_ids = [
        "1__5382617241__227642622",
        "1__7370776212__299794970",
        "1__13848730793__545226246",
        "1__13951953339__253482297",
        "1__9943772020__291306617",
        "1__13548704707__545226246",
    ]
    async with async_session() as db:
        for id in product_base_ids:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"https://apiv3.beecost.vn/product/review?product_base_id={id}&limit=5&page=0&review_type=0&type=new"
                )
                if response.status_code == 200:
                    reviews_data = response.json()["data"]["reviews"]
                    for review in reviews_data:
                        review_db = await db.scalar(
                            select(ProductReview).where(
                                ProductReview.review_base_id
                                == review["review_base_id"],
                                ProductReview.product_base_id
                                == review["product_base_id"],
                            )
                        )
                        if review_db is None:
                            product_review_obj = ProductReview(
                                review_base_id=review["review_base_id"],
                                product_base_id=review["product_base_id"],
                                platform_id=review["platform_id"],
                                title=review["title"],
                                content=review["content"],
                                rating=review["rating"],
                                images=review["images"],
                                created_at_platform=review["created_at_platform"],
                                user_username=review["user_username"],
                                user_url_image=review["user_url_image"],
                            )
                            db.add(product_review_obj)

        await db.commit()


async def crawl_product_insight():
    product_base_ids = [
        "1__5382617241__227642622",
        "1__7370776212__299794970",
        "1__13848730793__545226246",
        "1__13951953339__253482297",
        "1__9943772020__291306617",
        "1__13548704707__545226246",
    ]
    async with async_session() as db:
        for id in product_base_ids:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"https://apiv3.beecost.vn/product/detail?product_base_id={id}&type=new"
                )
                if response.status_code == 200:
                    product_insight_data = response.json()["data"]["product_base"][
                        "price_insight"
                    ]
                    product_insight_db = await db.scalar(
                        select(ProductPriceInsight).where(
                            ProductPriceInsight.product_base_id
                            == product_insight_data["product_base_id"]
                        )
                    )
                    if product_insight_db is None:
                        product_insight_obj = ProductPriceInsight(
                            product_base_id=product_insight_data["product_base_id"],
                            classify_price=product_insight_data["classify_price"],
                            current_price=product_insight_data["current_price"],
                            ratio=product_insight_data["ratio"],
                            max_price=product_insight_data["max_price"],
                            min_price=product_insight_data["min_price"],
                            delta_price=product_insight_data["delta_price"],
                        )
                        db.add(product_insight_obj)

        await db.commit()


async def main() -> None:
    logger.info("Crawling products")
    await crawl_products()
    logger.info("Crawling done")

    logger.info("Crawling product price history")
    await crawl_product_price_history()
    logger.info("Crawling done")

    logger.info("Crawling product review")
    await crawl_product_review()
    logger.info("Crawling done")

    logger.info("Crawling product insight")
    await crawl_product_insight()
    logger.info("Crawling done")


if __name__ == "__main__":
    asyncio.run(main())
