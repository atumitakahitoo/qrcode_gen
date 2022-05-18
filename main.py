# QR Code Generator
# PyQRCodeNG version https://github.com/pyqrcode/pyqrcodeNG

import streamlit as st
import pyqrcodeng as pyqrcode
from PIL import Image

QR_FILE = 'qrcode.png'
QR_CODE_COLOR = (80, 20, 80, 255)
BACKGROUND_COLOR = (250, 250, 250, 255)

st.title('QRコード作成アプリ')
st.subheader('You can generate a QR code from a string or URL.')
st.text('PyQRCodeNG version')
qr_url = st.text_input('Enter a string or URL to generate a QR code:', value='https://code2create.club/')

col1, col2 = st.columns(2)
with col1:
    qr_version = st.slider('Version (1-10)', 1, 10, value=5)
    qr_correction = st.select_slider(
                        "Error Correction Grade: [L, M, Q, H]",
                        options=['L', 'M', 'Q', 'H'], value='H')
    qr_scale = st.slider('Scale (4-8 pixels/cell)', 2, 8, value=4)
    st.text(f'Length: {len(qr_url)}')
    st.text(f'QR Code Version: {qr_version}')
    st.text(f'Error Correction Grade: {qr_correction}')
    st.text(f'Mode: Scale: {qr_scale}')

try:
    qr = pyqrcode.create(qr_url, error=qr_correction, version=qr_version, mode='binary')
    qr.png(QR_FILE, scale=qr_scale, module_color=QR_CODE_COLOR, background=BACKGROUND_COLOR, quiet_zone=4)
    img = Image.open(QR_FILE)
    with col2:
        st.image(img)
except pyqrcode.DataOverflowError:
    with col2:
        st.error(f'Character length {len(qr_url)} is too long to fit within the QR Code.')
        st.error('Error: Data Overflow. Please try again with a larger version number or a lower Error Correction Grade')
        st.error('エラー：データあふれ　バージョンを上げたり、エラー訂正のグレードを下げてお試しください。')
except Exception as e:
    st.write(e)
