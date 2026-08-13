import streamlit as st
from ollama import chat
from PIL import Image
import tempfile
import os

st.title("🖼️ AI图片识别助手")

uploaded_file = st.file_uploader(
    "请选择图片",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # 显示图片
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="上传的图片",
        use_container_width=True
    )

    # 保存图片
    image_bytes = uploaded_file.getvalue()

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as tmp_file:

        tmp_file.write(image_bytes)
        image_path = tmp_file.name

    # 调试信息
    st.write("图片路径：", image_path)
    st.write("图片大小：", os.path.getsize(image_path), "bytes")

    question = st.text_input(
        "请输入问题",
        value="请描述这张图片"
    )

    if st.button("开始分析"):

        try:

            with st.spinner("AI分析中..."):

                response = chat(
                    model="llava",
                    messages=[
                        {
                            "role": "user",
                            "content": question,
                            "images": [image_path]
                        }
                    ]
                )

                answer = response["message"]["content"]

            st.subheader("分析结果")
            st.write(answer)

        except Exception as e:

            st.error(str(e))