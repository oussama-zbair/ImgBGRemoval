# ImgBGRemoval

[![Build Status](https://img.shields.io/travis/your-username/ImgBGRemoval/master.svg?style=flat-square)](https://travis-ci.org/your-username/ImgBGRemoval)
[![License](https://img.shields.io/github/license/your-username/ImgBGRemoval.svg?style=flat-square)](https://github.com/your-username/ImgBGRemoval/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/your-username/ImgBGRemoval.svg?style=flat-square)](https://github.com/your-username/ImgBGRemoval/issues)
[![GitHub stars](https://img.shields.io/github/stars/your-username/ImgBGRemoval.svg?style=flat-square)](https://github.com/your-username/ImgBGRemoval/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/your-username/ImgBGRemoval.svg?style=flat-square)](https://github.com/your-username/ImgBGRemoval/network)
[![GitHub contributors](https://img.shields.io/github/contributors/your-username/ImgBGRemoval.svg?style=flat-square)](https://github.com/your-username/ImgBGRemoval/graphs/contributors)
[![Twitter](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fyour-username%2FImgBGRemoval.svg?style=flat-square)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fyour-username%2FImgBGRemoval)
[![GitHub last commit](https://img.shields.io/github/last-commit/your-username/ImgBGRemoval.svg?style=flat-square)](https://github.com/your-username/ImgBGRemoval/commits/master)
[![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-2.0-green.svg?style=flat-square)](https://flask.palletsprojects.com/en/2.0.x/)
[![U2Net Model](https://img.shields.io/badge/U2Net-Deep%20Learning-orange.svg?style=flat-square)](https://github.com/xuebinqin/U-2-Net)
[![Netlify Status](https://api.netlify.com/api/v1/badges/your-netlify-site-id/status.svg?style=flat-square)](https://app.netlify.com/sites/your-netlify-site-id)

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

3. **Run the Flask application:**

    ```bash
    flask run
    ```

## Screenshots

### Home Page
![Home Page](static/screenshots/home_page.png)

### Upload Image
![Upload Image](static/screenshots/upload_image.png)

### Processed Image
![Processed Image](static/screenshots/processed_image.png)

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
