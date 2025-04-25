from config.build_storage import get_storage
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.prompts import PromptTemplate

prompt = PromptTemplate("""\
    Bạn là trợ lý có khả năng trả về các thông tin sản phẩm đang có. \n
    Bạn hãy trả lời câu hỏi cho ngắn gọn thú vị dựa trên đặc điểm cá nhân của người dùng và ngữ cảnh sau {context_str}. \n
    Đây là câu hỏi: {query_str}.
    Trả lời: 
""")

index = get_storage("./pure_db")
retriever = index.as_retriever()
query_engine = RetrieverQueryEngine.from_args(retriever, text_qa_template=prompt)

while True:
    query = input("Bạn hãy nhập câu hỏi: ")
    response = query_engine.query(query)
    print(response)