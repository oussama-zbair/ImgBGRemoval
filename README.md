# ImgBGRemoval

[![License](https://img.shields.io/github/license/oussama-zbair/ImgBGRemoval.svg?style=flat-square)](https://github.com/oussama-zbair/ImgBGRemoval/blob/master/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/oussama-zbair/ImgBGRemoval.svg?style=flat-square)](https://github.com/oussama-zbair/ImgBGRemoval/commits/master)
[![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-2.0-green.svg?style=flat-square)](https://flask.palletsprojects.com/en/2.0.x/)
[![U2Net Model](https://img.shields.io/badge/U2Net-Deep%20Learning-orange.svg?style=flat-square)](https://github.com/xuebinqin/U-2-Net)

ImgBGRemoval is a Flask-based web application designed to simplify background removal from images. With just a few clicks, users can upload images and effortlessly remove backgrounds.

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

[![Home Page](https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/1.PNG)](https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/1.PNG)
[![Upload Image](https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/2.PNG)](https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/2.PNG)
[![Processed Image](https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/3.PNG)](https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/3.PNG)
[![Upload Image](https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/4.PNG)](https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/4.PNG)
[![Processed Image](https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/5.PNG)](https://github.com/oussama-zbair/ImgBGRemoval/blob/main/static/screenshots/5.PNG)

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
