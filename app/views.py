from flask import render_template, request, flash, redirect, url_for
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
    
    # Check if the data is empty
    if not data:
        # Flash a message to prompt the user to enter a URL
        flash('Please enter a URL.')
        # Redirect the user back to the index page
        return redirect(url_for('index'))

    # Generate QR code
    qr = qrcode.make(data)
    buffered = BytesIO()
    qr.save(buffered, format="PNG")
    qr_img_bytes = base64.b64encode(buffered.getvalue()).decode('utf-8')

    # Render the QR code template with the QR image data and the input data
    return render_template('qr_code.html', qr_img_data=qr_img_bytes, data=data)
