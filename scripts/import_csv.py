import csv
from pathlib import Path
from sqlalchemy.orm import Session

from app.core.settings.database import SessionLocal
from app.core.settings.logging import logger
from app.models.product import Product
from app.enums.locations import LocationEnum


BASE_DIR = Path(__file__).resolve().parent.parent
CSV_FILE_PATH = BASE_DIR / "data" / "items.csv"


def parse_float(value: str) -> float:
    try:
        return float(value)
    except Exception:
        return 0.0


def parse_location(value: str) -> LocationEnum:
    try:
        return LocationEnum(value)
    except Exception:
        raise ValueError(f"Invalid location value: {value}")


def row_to_product_data(row: dict):
    return {
        "id": int(row["id"]),
        "title": row["title"].strip(),
        "description": row["description"].strip(),
        "price": parse_float(row["price"]),
        "location": parse_location(row["location"]),
    }


def get_product(db: Session, product_id: int):
    return db.get(Product, product_id)


def is_different(db_product: Product, new_data: dict) -> bool:
    return (
        db_product.title != new_data["title"]
        or db_product.description != new_data["description"]
        or float(db_product.price) != float(new_data["price"])
        or db_product.location != new_data["location"]
    )


def upsert_products(db: Session, csv_file_path: Path):
    updated = 0
    skipped = 0
    inserted = 0

    with open(csv_file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data = row_to_product_data(row)

            db_product = get_product(db, data["id"])

            if not db_product:
                product = Product(
                    id=data["id"],
                    title=data["title"],
                    description=data["description"],
                    price=data["price"],
                    location=data["location"],
                )
                db.add(product)
                inserted += 1
                continue

            # if
            if is_different(db_product, data):
                db_product.title = data["title"]
                db_product.description = data["description"]
                db_product.price = data["price"]
                db_product.location = data["location"]

                updated += 1
            else:
                skipped += 1

    db.commit()

    logger.info("\n=== Import Summary ===")
    logger.info(f"Inserted: {inserted}")
    logger.info(f"Updated: {updated}")
    logger.info(f"Skipped: {skipped}")


def main():
    db = SessionLocal()
    try:
        upsert_products(db, CSV_FILE_PATH)
    finally:
        db.close()


if __name__ == "__main__":
    main()