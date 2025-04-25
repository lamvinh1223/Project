# print("Import công cụ chat")
# from chat import chat_engine
# print("Hoàn thành load thư viện")

import streamlit as st
from config.build_storage import get_storage

def get_chat_engine():
    index = get_storage("./data/normal_store_index")
    chatbot = index.as_chat_engine()
    return chatbot

# Hàm phản hồi chatbot
def chatbot_response(user_input, chat_engine):
    # Giả lập chatbot trả lời
    response = chat_engine.chat(user_input)
    return f"AI: {response.response}"

# Tiêu đề giao diện
st.title("Mychatbot")

# Lấy chatbot
chat_engine = get_chat_engine()

# Khu vực nhập liệu từ người dùng
user_input = st.text_input("Nhập câu hỏi:")

if user_input:
    # Hiển thị câu trả lời của chatbot
    response = chatbot_response(user_input, chat_engine)
    st.write(response)
