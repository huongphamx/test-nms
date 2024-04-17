from app.utils import generate_base58


def generate_prefix_id(prefix: str):
    prefix_id = prefix + generate_base58(length=11)
    return prefix_id
