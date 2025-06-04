
import streamlit as st
import json

def load_components():
    with open("b787_hydraulic_components_db.json") as f:
        return json.load(f)

components = load_components()

st.set_page_config(page_title="B787 Chatbot", layout="centered")
st.title("B787 Hydraulic Systems Chatbot")
st.markdown("اسألني عن أي مكون في نظام الهيدروليك للطائرة B787")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.chat_input("اكتب سؤالك هنا...")

def answer_question(q):
    q = q.lower()
    for key, comp in components.items():
        if key in q or comp["name"].lower() in q:
            return f"""**{comp['name']}**
- النظام: {', '.join(comp['system'])}
- النوع: {comp['type']}
- الوظيفة: {comp['function']}
- الموقع: {comp['location']}
- الضغط: {comp['pressure']}
- ملاحظات: {comp['notes']}"""
    return "عذرًا، لم أجد هذا المكون في قاعدة البيانات."

if user_input:
    st.session_state.history.append(("أنت", user_input))
    response = answer_question(user_input)
    st.session_state.history.append(("المساعد", response))

for speaker, text in st.session_state.history:
    with st.chat_message("👤" if speaker == "أنت" else "🤖"):
        st.markdown(text)
