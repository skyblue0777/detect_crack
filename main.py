import streamlit as st
import numpy as np
import pandas as pd
import sklearn
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

st.line_chart(df)


st.text('hiaaaaa')
st.text('hiaaaaa')
st.text('hiaaaaa')

import matplotlib.pyplot as plt

# 데이터 생성
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 선 그래프 그리기
plt.plot(x, y)

# 그래프에 제목과 레이블 추가
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

print('hihihi')
