import streamlit as st
from ollama import chat
from PIL import Image
import tempfile

st.title("🖼️ AI图片识别助手")

# 上传图片
uploaded_file = st.file_uploader(
    "请选择图片",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    # 显示图片
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="上传的图片",
        use_container_width=True
    )

    # 保存临时文件
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".jpg"
    ) as tmp_file:

        tmp_file.write(uploaded_file.read())
        image_path = tmp_file.name

    # 输入问题
    question = st.text_input(
        "请输入你想问的问题",
        "请描述这张图片"
    )

    # 按钮
    if st.button("开始分析"):

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