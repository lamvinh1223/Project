import json

product_infors = ["data/raw/products/product.json", "data/raw/products/product-sachvavanphongpham.json"]
from config.build_storage import describe_product, get_nodes_2, build_storage

def describe_book(book):
  _title = book["property"]["name"]
  _type_book = book["property"]["type"]
  _rating = book["property"]["rating"]
  _cost = book["cost"]
  _description = book["description"]

  title = f"Sản phẩm với tên {_title} thuộc thể loại 'Sách và văn phòng phẩm'."
  cost = f"Sản phẩm này có giá {_cost}VNĐ."
  rating = f"Sản phẩm được đánh giá là {_rating}."
  _type=  f"Sản phẩm này thuộc thể loại {_type_book}."
  description = f"Mô tả sản phẩm: {_description}"

  return title + ' ' + _type + ' ' + rating + ' ' + cost + ' ' + description

describe_functions = [describe_product, describe_book]

tempoary = []
for product_infor, get_describe in zip(product_infors, describe_functions):
  with open(product_infor, "rb") as f:
    tempoary += json.load(f)["products"]
described_product = [get_describe(product) for product in tempoary]
nodes = get_nodes_2(described_product)
index = build_storage(nodes, "./pure_db")