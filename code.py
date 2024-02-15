import streamlit as st
import qrcode
from PIL import Image
import io

st.write('hello')
url = "https://uscapston.streamlit.app/"

# QR 코드 생성
qr_code = qrcode.make(url)

# PIL 이미지로 변환
img_pil = qr_code.get_image()

# 이미지를 바이트로 변환
img_byte_arr = io.BytesIO()
img_pil.save(img_byte_arr, format='PNG')
img_byte_arr = img_byte_arr.getvalue()

# 스트림릿 앱에 이미지 표시
st.image(img_byte_arr, use_column_width=True)




