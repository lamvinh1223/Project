# from google.generativeai import GenerativeModel
from llama_index.llms.gemini import Gemini
from .constant import EMBED_MODEL_NAME, LLM_MODEL_NAME
# from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings
# from llama_index.llms.llama_cpp import LlamaCPP


# llm = HuggingFaceLLM(model_name=LLM_MODEL_NAME, tokenizer_name=LLM_MODEL_NAME, model_kwargs={"use_auth_token": ""})
# llm = HuggingFaceInferenceAPI(model_name=LLM_MODEL_NAME, token="")
# llm = LlamaCPP(model_path="./ggml-vistral-7B-chat-q4_1.gguf", temperature=0.5, max_new_tokens=512, context_window=2048, model_kwargs={
#     "n_threads" : 4
# })
# llm = GenerativeModel()
llm = Gemini(api_key="")

embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL_NAME)

Settings.llm = llm
Settings.embed_model = embed_model

# output = llm.complete("Bạn giới thiệu về bạn nhe")
# print(output)