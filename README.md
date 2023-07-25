# Image-Steganography-GUI
Image Steganography is a simple Python-based GUI application that allows users to hide secret messages within images using the Least Significant Bit (LSB) technique. The hidden message can later be retrieved from the image.

## Requirements
To run the Image Steganography project, you need to have the following software installed on your machine:

1. Python 3.x
2. Tkinter
3. Pillow (PIL)
4. stegano

## Installation
1. Clone the repository to your local machine.
2. Install the required Python libraries by running the following command in your terminal:
```Python
pip install tkinter pillow stegano
```

## How to Use
1. Run the steganography.py file to launch the GUI application.
2. The application window will open, displaying the "Image Steganography" title and interface.
3. Click on the "Select Image" button to choose an image file from your local system. Supported formats are PNG, JPG, and JPEG.
4. Enter the secret message you want to hide in the "Input/Output of Secret Message" text box.
5. Click on the "Hide Message" button to embed the secret message into the selected image.
6. To save the image with the hidden message, enter the desired file name in the "Input of Output File Name" text box, and click the "Save Image" button.
7. To reveal the hidden message from the image, click the "Show Message" button. The message will be displayed in the "Input/Output of Secret Message" text box.
8. You can reset the fields and image by clicking the "Reset" button.
