import streamlit as st
import os
from google import genai

os.environ["GEMINI_API_KEY"] = st.secrets["gemini"]["api_key"]
client = genai.Client()

text = st.text_input("質問")
if st.button("実行", use_container_width=True):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"赤ちゃん言葉で答えてください。{text}"
    )
    st.write(response.text)
