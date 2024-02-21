import streamlit as st
from PIL import Image

def main():
    st.title("Streamlit Image Upload and Display")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # 업로드한 파일을 이미지로 변환
        image = Image.open(uploaded_file)

        # 이미지를 화면에 출력
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        exec(open('test.py').read())

if __name__ == "__main__":
    main()
