import json
from typing import List
from llama_index.core import Document, VectorStoreIndex, load_index_from_storage, StorageContext
from .enhance_document import *

# Cấu hình xây dựng tài liệu
def describe_product(product_infor):
    product_title = product_infor["property"]["name"]
    actual_cost = product_infor["cost"]
    rating_score = product_infor["property"]["rating"]
    product_type = product_infor["property"]["type"]
    product_gender = product_infor["property"]["gender"]
    product_color = product_infor["property"]["color"]
    description_product = product_infor["description"]


    title = f"Sản phẩm với tên {product_title}."
    cost = f"Sản phẩm '{product_title}' có giá là: {actual_cost} VNĐ."
    rate = f"Sản phẩm '{product_title}' được đánh giá với số điểm {rating_score}."
    _type = f"Sản phẩm '{product_title}' thuộc loại sản phẩm {product_type}."
    _gender = f"Sản phẩm '{product_title}' dành cho {product_gender}."
    _color = f"Sản phẩm '{product_title}' có màu sắc là {product_color}."
    description = f"Mô tả sản phẩm '{product_title}' : {description_product}."
    categories = f"Sản phẩm '{product_title}' có thể được phân thành các danh mục: {', '.join(product_infor['category'])}"

    product = title + ' ' + _type + ' ' + _gender + ' ' + _color + ' ' + description + ' ' + cost + ' ' + rate + ' ' + categories
    return product

def get_nodes(described_products : List[str]):
    docs = [Document(text=product) for product in described_products]
    nodes = default_ingestion_pipeline.run(documents=docs)
    return nodes 

def get_nodes_2(described_products : List[str]):
    docs = [Document(text=product) for product in described_products]
    nodes = simple_pipeline.run(documents=docs)
    return nodes 

def build_storage(nodes, storage_path) -> VectorStoreIndex:
    index = VectorStoreIndex(nodes)
    index.storage_context.persist(persist_dir=storage_path)
    return index

def get_storage(storage_path) -> VectorStoreIndex:
    storage_context = StorageContext.from_defaults(persist_dir=storage_path)
    index : VectorStoreIndex = load_index_from_storage(storage_context)
    return index

if __name__ == "__main__":
    # _product_path = "E:/chatbot-brainy-bots/products/first.json"
    # describe_product(_product_path)
    pass