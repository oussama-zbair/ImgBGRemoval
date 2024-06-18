# ImgBGRemoval

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

The application uses the U2Net deep learning model to perform precise image segmentation for background removal. Here's a brief overview of the process:

1. **Image Upload**: Users upload an image to the web application.
   
2. **Image Processing**: The uploaded image undergoes preprocessing and is fed into the U2Net model, which generates a binary mask indicating the foreground (object) and background.
   
3. **Background Removal**: Using the generated mask, the application removes the background from the image, creating a transparent background.
   
4. **Result Display and Download**: Users can view the original and processed images on the web interface. They have the option to download the processed image with the transparent background.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License.
