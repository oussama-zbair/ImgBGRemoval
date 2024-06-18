import os
import cv2
from numpy import array, uint8
from flask import Flask, render_template, request, redirect, send_from_directory, jsonify, url_for
from PIL import Image
import torch
from torchvision import transforms
from models.u2net import U2NET

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

filename_counter = 0

# Load the U2Net model
model_path = 'models/u2net.pth'
net = U2NET(3, 1)
net.load_state_dict(torch.load(model_path, map_location='cpu'))
net.eval()


def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((320, 320)),
        transforms.ToTensor()
    ])
    return transform(image).unsqueeze(0)


def postprocess_mask(mask, original_size):
    mask = mask.squeeze().cpu().numpy()
    mask = cv2.resize(mask, original_size, interpolation=cv2.INTER_LINEAR)
    return (mask > 0.5).astype(uint8)


def remove_background(image_path):
    image = Image.open(image_path).convert('RGBA')  # Open image and convert to RGBA
    original_size = image.size
    input_tensor = preprocess_image(image_path)

    with torch.no_grad():
        d1, _, _, _, _, _, _ = net(input_tensor)  # Assuming U2NET returns a tuple with multiple outputs
        mask = d1[:, 0, :, :]
        mask = postprocess_mask(mask, original_size)

    image_np = array(image)

    # Create a transparent background where the mask is zero
    image_np[:, :, 3] = mask * 255

    result_image = Image.fromarray(image_np, 'RGBA')

    return result_image


def generate_filename():
    global filename_counter
    filename = f'image_processed_{filename_counter}.png'  # Save as PNG to support transparency
    filename_counter += 1
    return filename


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = generate_filename()
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            result_image = remove_background(file_path)
            result_filename = generate_filename()
            result_path = os.path.join(app.config['UPLOAD_FOLDER'], result_filename)
            result_image.save(result_path)

            return jsonify({
                'filename': filename,
                'result_filename': result_filename,
                'upload_url': url_for('static', filename='uploads/') + '/',
                'download_url': url_for('download_file', filename='') + '/'
            })
    return render_template('index.html')


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
