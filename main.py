import streamlit as st
from PIL import Image
# YOLOv5 PyTorch HUB Inference (DetectionModels only)
import torch
import os

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
        
        # model = torch.hub.load('./yolov5', 'custom',  'yolov5s.pt', source='local')  # yolov5n - yolov5x6 or custom
        # im = './test.png'  # file, Path, PIL.Image, OpenCV, nparray, list
        # results = model(im)  # inference
        # results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
        # st.write("This is a simple Streamlit app.")

        # model = torch.hub.load('./yolov5-master', 'custom',  'best.pt')  # yolov5n - yolov5x6 or custom
        model = torch.hub.load('/yolov5-master', 'custom', path='best.pt')
        # model = torch.hub.load('./yolov5-master', 'custom',  'best.pt', source='local')  # yolov5n - yolov5x6 or custom
        # model = torch.hub.load('./yolov5-master', 'best.pt', force_reload=True, trust_repo=True)  # or yolov5n - yolov5x6 or custom
        im = 'https://ultralytics.com/images/zidane.jpg'  # file, Path, PIL.Image, OpenCV, nparray, list
        results = model(im)  # inference
        st.image(results, caption="Uploaded Image.", use_column_width=True)
        # results = model(image)  # inference
        # st.image(results, caption="Uploaded Image.", use_column_width=True)

        # st.write(results)


if __name__ == "__main__":
    main()
