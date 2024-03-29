import streamlit as st
import sys
st.write('파이썬 버전 : ', sys.version)

from PIL import Image
# YOLOv5 PyTorch HUB Inference (DetectionModels only)
import torch
import os
# from models.experimental import attempt_load

def main():
    st.title("도장 결함 검출 프로그램")
    st.write(os.getcwd())
    uploaded_file = st.file_uploader("Choose an image...", type="png")

    if uploaded_file is not None:
        # 업로드한 파일을 이미지로 변환
        image = Image.open(uploaded_file)

        # 이미지를 화면에 출력
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        exec(open('test.py').read())
        
        # YOLOv5 모델 초기화
        model = torch.load('./yolov5-master/best.pt', map_location=torch.device('cuda' if torch.cuda.is_available() else 'cpu'))

        
        im = 'https://ultralytics.com/images/zidane.jpg'  # file, Path, PIL.Image, OpenCV, nparray, list
        results = model(im)  # inference
        st.image(results, caption="Uploaded Image.", use_column_width=True)
        # results = model(image)  # inference
        # st.image(results, caption="Uploaded Image.", use_column_width=True)

        # st.write(results)


if __name__ == "__main__":
    main()
