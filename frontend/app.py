import streamlit as st
import requests

st.title("✉️ Email Reply Agent")

email_input = st.text_area("Paste the original email:")
tone = st.selectbox("Select tone:", ["Formal", "Casual", "Friendly", "Professional"])
length = st.selectbox("Select length:", ["Short", "Medium", "Long"])

if st.button("Generate Reply"):
    if not email_input.strip():
        st.warning("Please paste an email to reply to.")
    else:
        response = requests.post(
            "http://localhost:8000/generate",
            json={"email": email_input, "tone": tone, "length": length}
        )
        reply = response.json().get("reply", "No reply generated.")
        st.success("✉️ Generated Reply:")
        st.write(reply)
