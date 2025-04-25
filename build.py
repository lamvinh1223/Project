from config.constant import BUILT_STORAGE

if not BUILT_STORAGE:
    from config.build_storage import describe_product, get_nodes, build_storage

    _product_path = "E:/chatbot-brainy-bots/products/first.json"
    product = describe_product(_product_path)
    nodes = get_nodes([product])
    index = build_storage(nodes, "./db")

else:
    from config.build_storage import get_storage
    index = get_storage("./db")