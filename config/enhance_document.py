from .model import *
from llama_index.core.node_parser import SemanticSplitterNodeParser, SentenceSplitter
from llama_index.core.node_parser.text import SentenceSplitter as TextSentenceSplitter, SemanticSplitterNodeParser as TextSemanticSplitterNodeParser
from llama_index.core.extractors import TitleExtractor, SummaryExtractor, QuestionsAnsweredExtractor
from llama_index.core.ingestion import IngestionPipeline

txt_sentence_splitter = TextSentenceSplitter(separator='.', chunk_size=50, chunk_overlap=10)
txt_semantic_sentence_splitter = TextSemanticSplitterNodeParser(embed_model=embed_model, breakpoint_percentile_threshold=75)
sentence_splitter = SentenceSplitter(separator=".", chunk_size=50, chunk_overlap=10)
semantic_splitter = SemanticSplitterNodeParser(embed_model=embed_model, breakpoint_percentile_threshold=80)

node_title_template = """\
Ngữ cảnh: {context_str}. Hãy cung cấp tiêu đề cái mà tổng hợp hết tất cả những thông tin đặc biệt \
và nổi bật trong ngữ cảnh đó.
"""

node_title_combine_template = """\
{context_str}. Dựa trên những thông tin ở trên. Hãy sinh ra tiêu đề phù hợp nhất \
cho dữ liệu đã được cung cấp. Tiêu đề:
"""

summary_template = """\
Dưới đây là thông tin của phần được cung cấp
{context_str}

Hãy tóm tắt lại nội dung của thông tin được cung cấp trên một cách ngắn gọn đặc sắc từ

Kết quả:
"""

question_answered_template = """\
Dưới đây là nội dung:
{context_str}

Chỉ được dựa trên thông tin trong ngữ cảnh này, \
hãy tạo ra {num_questions} câu hỏi mà ngữ cảnh này có thể cung cấp \
câu trả lời cụ thể, và những câu trả lời này khó có thể tìm thấy ở nơi khác.

Các tóm tắt ở mức độ cao của ngữ cảnh xung quanh cũng có thể được cung cấp. \
Hãy thử sử dụng những tóm tắt này để tạo ra các câu hỏi tốt hơn mà ngữ cảnh này có thể trả lời.
"""

title_extractor = TitleExtractor(node_template=node_title_template, combine_template=node_title_combine_template)
summary_extractor = SummaryExtractor(prompt_template=summary_template)
question_answered_extractor = QuestionsAnsweredExtractor(prompt_template=question_answered_template, questions=3)

default_ingestion_pipeline = IngestionPipeline(name="Phương pháp 1", 
    transformations=[
        semantic_splitter,
        title_extractor,
        summary_extractor,
        question_answered_extractor
    ])

simple_pipeline = IngestionPipeline(name = "Phương pháp 2", 
                                    transformations=[
                                        semantic_splitter
                                    ])

# summary_extractor_ingestion_pipeline = IngestionPipeline(name="Phương pháp 2", 
#     transformations=[
#         semantic_splitter,
#         summary_extractor
#     ])

# question_answered_pipeline = IngestionPipeline(name="Phương pháp 3", 
#     transformations=[
#         semantic_splitter,
#         question_answered_extractor
#     ])