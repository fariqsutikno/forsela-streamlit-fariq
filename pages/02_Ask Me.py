# from transformers import AutoModel, AutoTokenizer, pipeline
# from langchain.utilities import WikipediaAPIWrapper
import streamlit as st

st.title("Forsela AI Chatbot")
st.write("Coming Soon")

# # model_name = "deepset/roberta-base-squad2"
# # model = AutoModelForQuestionAnswering.from_pretrained(model_name)
# # tokenizer = AutoTokenizer.from_pretrained(model_name)

# # model_name = "deepset/roberta-base-squad2"

# # # a) Get predictions
# # nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)


# # b) Load model & tokenizer

# tokenizer = AutoTokenizer.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
# model = AutoModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")

# nlp = pipeline("document-question-answering", model="naver-clova-ix/donut-base-finetuned-docvqa")

# question_input = st.text_input("Question:")

# if question_input:
#     keywords = question_input.split()

#     QA_input = {
#     'question': 'question_input',
#     'context': 'Gunakan bahasa Indonesia. Kamu adalah asisten kepala sekolah MAS Al Irsyad yang bernama Forsela. Bersikaplah ramah dan Islami. Kamu hanya bisa menjawab soal yang berkaitan pada file yang dilampirkan.'
#     }
#     res = nlp(QA_input)

#     st.text_area("Answer:", res['answer'])
#     st.write("Score:", res['score'])