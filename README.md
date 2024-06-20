# ImgBGRemoval

<p align="center">
  <img src="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/logo.png" alt="ImgBGRemoval Logo" width="200">
</p>

<p align="center">
  <a href="https://github.com/oussama-zbair/ImgBGRemoval/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/oussama-zbair/ImgBGRemoval.svg?style=for-the-badge" alt="License">
  </a>
  <a href="https://github.com/oussama-zbair/ImgBGRemoval/commits/master">
    <img src="https://img.shields.io/github/last-commit/oussama-zbair/ImgBGRemoval.svg?style=for-the-badge" alt="GitHub last commit">
  </a>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/python-3.7%20%7C%203.8-blue.svg?style=for-the-badge" alt="Python Version">
  </a>
  <a href="https://flask.palletsprojects.com/en/2.0.x/">
    <img src="https://img.shields.io/badge/flask-2.0-green.svg?style=for-the-badge" alt="Flask Version">
  </a>
  <a href="https://github.com/xuebinqin/U-2-Net">
    <img src="https://img.shields.io/badge/U2Net-Deep%20Learning-orange.svg?style=for-the-badge" alt="U2Net Model">
  </a>
  <a href="https://github.com/oussama-zbair/ImgBGRemoval/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/oussama-zbair/ImgBGRemoval/ci.yml?style=for-the-badge" alt="CI Status">
  </a>
</p>

<p align="center">
  <strong>ImgBGRemoval</strong> is a Flask-based web application designed to simplify background removal from images. With just a few clicks, users can upload images and effortlessly remove backgrounds.
</p>

## Features

- **Upload images** to remove background.
- **Process uploaded images** using the U2Net deep learning model.
- **Download processed images** with transparent backgrounds.

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (jQuery)
- **Backend**: Python, Flask
- **Deep Learning Model**: U2Net
- **Libraries**: OpenCV, PIL (Python Imaging Library), PyTorch (for deep learning)
- **Deployment**: Netlify (frontend), Flask server (backend)

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/ImgBGRemoval.git
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Download U2Net model files:**

    - Download the `u2net.pth` model file from the [U2Net repository](https://github.com/xuebinqin/U-2-Net).
    - Create a directory named `models` in the root of your project and place the `u2net.pth` file inside it.

4. **Run the Flask application:**

    ```bash
    flask run
    ```

## Screenshots

<p align="center">
  <a href="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/1.PNG">
    <img src="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/1.PNG" alt="Home Page" width="200">
  </a>
  <a href="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/2.PNG">
    <img src="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/2.PNG" alt="Upload Image" width="200">
  </a>
  <a href="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/3.PNG">
    <img src="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/3.PNG" alt="Processed Image" width="200">
  </a>
  <a href="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/4.PNG">
    <img src="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/4.PNG" alt="Upload Image" width="200">
  </a>
  <a href="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/5.PNG">
    <img src="https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/5.PNG" alt="Processed Image" width="200">
  </a>
</p>

## How It Works

The application uses the [U2Net](https://github.com/xuebinqin/U-2-Net "U2Net") deep learning model to perform precise image segmentation for background removal. Here's a brief overview of the process:

1. **Image Upload**: Users upload an image to the web application.
2. **Image Processing**: The uploaded image undergoes preprocessing and is fed into the U2Net model, which generates a binary mask indicating the foreground (object) and background.
3. **Background Removal**: Using the generated mask, the application removes the background from the image, creating a transparent background.
4. **Result Display and Download**: Users can view the original and processed images on the web interface. They have the option to download the processed image with the transparent background.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
