from config.build_storage import get_storage
from llama_index.core.prompts import PromptTemplate

my_desired_response = PromptTemplate("""\
    Bạn là một trợ lí trả lời thông tin về sản phầm được lưu. \n
    Nếu có bịa thông tin thì bịa vừa vừa đừng lố quá. \n
    Bạn hãy trả lời dựa trên những thông tin cung cấp và lịch sử trò chuyện qua {context_str}. \n
    Đây là câu hỏi bạn nhận: {query_str}. \n
    Trả lời: 
""")

index = get_storage("./data/normal_store_index")
chat_engine = index.as_chat_engine(chat_prompt=my_desired_response)


if __name__ == "__main__":
    while True:
        query = input("Bạn muốn hỏi gì?")
        response = chat_engine.chat(query)
        print(f"Phản hồi: {response.response}")