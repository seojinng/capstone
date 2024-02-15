import streamlit as st
import streamlit_qrcode

# URL 설정
url = "https://uscapston.streamlit.app/"

# 스트림릿 앱에 QR 코드 이미지 표시
st.write(f"QR 코드를 스캔하여 이동하세요: {url}")
streamlit_qrcode.streamlit_qrcode(url)


