from flask import render_template, request
from app import app
import qrcode
import base64
from io import BytesIO

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr_code', methods=['POST'])
def generate_qr_code():
    data = request.form['data']
    qr = qrcode.make(data)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    qr_img_bytes = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return render_template('qr_code.html', qr_img_data=qr_img_bytes, data=data)
