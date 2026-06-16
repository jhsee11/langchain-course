from dotenv import load_dotenv
from langsmith import traceable


def get_product_price(product: str) -> str:
    """Look up the price of a product in the catalog"""
    print(f" >> Executing get_product_price tool for product: {product}")
    prices = {"laptop": 1000, "mouse": 10, "keyboard": 20}
    return prices.get(product, "Product not found")

def apply_discount(price: float, discount_tier: float) -> float:
    """Apply a discount tier to a price and return the discounted price"""
    print(f" >> Executing apply_discount tool for price: {price} and discount_tier: {discount_tier}")
    discount_percentages = {"bronze": 5, "silver": 12, "gold": 23}
    discount = discount_percentages.get(discount_tier, 0)
    return round(price * (1 - discount / 100), 2)

load_dotenv()

MAX_ITERATIONS = 10
MODEL = "gpt-5.4-mini"

@tool
def get_product_price(product: str) -> str:
    """Look up the price of a product in the catalog"""