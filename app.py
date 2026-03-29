import streamlit as st
from openai import OpenAI
from PIL import Image
import base64

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("📡 地震速報轉主播稿 AI")

uploaded_file = st.file_uploader("請上傳地震速報圖卡", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("生成主播稿"):
        with st.spinner("AI正在寫稿中..."):

            base64_image = base64.b64encode(uploaded_file.read()).decode("utf-8")

            response = client.responses.create(
                model="gpt-4o",
                input=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "input_text", "text": "請生成主播稿與標題"},
                            {"type": "input_image", "image_base64": base64_image}
                        ]
                    }
                ],
                max_output_tokens=500
            )

            result = response.output_text
            st.write(result)
