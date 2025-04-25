import json
from config.constant import BUILT_STORAGE, PRODUCT_PATH, STORAGE_VECTOR_STORE_DATA

# Lấy dữ liệu sản phẩm và xây dựng cơ sở truy vấn
if not BUILT_STORAGE:
    from config.build_storage import describe_product, get_nodes_2, build_storage, get_storage

    with open(PRODUCT_PATH, "r", encoding="utf-8") as f:
      products = json.load(f)["products"]
    print("Tổng số sản phẩm: ", len(products))
    described_product = [describe_product(product) for product in products]
    nodes = get_nodes_2(described_product)
    index = build_storage(nodes, "./pure_db")
else:
    index = get_storage(STORAGE_VECTOR_STORE_DATA)