if st.button("生成主播稿"):
    with st.spinner("AI正在寫稿中..."):

        base64_image = base64.b64encode(uploaded_file.read()).decode("utf-8")

        response = client.responses.create(
            model="gpt-4o",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "請根據地震圖生成主播稿"
                        },
                        {
                            "type": "input_image",
                            "image_base64": base64_image
                        }
                    ]
                }
            ],
            max_output_tokens=500
        )

        result = response.output_text
        st.write(result)
