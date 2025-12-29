import streamlit as st
import requests


st.set_page_config(page_title="gym assistant")
st.title("💪🏋️‍♀️ SWEAT SMART")
st.write("Fuel your fitness journey with high-fiber foods that work as hard as you do")


API_URL = "http://192.168.27.162:1234/v1/chat/completions"

def ask_model(user_question):
    payload = {
        "model": "gemma",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a gym guidance assistant. "
                    "Give clear, simple advice about fiber-rich foods, "
                    "pre-workout and post-workout nutrition. "
                    "Focus on Indian vegetarian foods when possible. "
                    "Do not give medical advice."
                )
            },
            {
                "role": "user",
                "content": user_question
            }
        ],
       
    }

    response = requests.post(API_URL, json=payload)
    result = response.json()
    return result["choices"][0]["message"]["content"]


user_input = st.text_input("Ask your question")


if user_input:
    try:
        answer = ask_model(user_input)
        st.success(answer)
    except Exception as e:
      pass
