# Image Processing with Gamma Correction

## Overview
This project demonstrates basic image processing techniques, focusing on gamma correction. The script utilizes the OpenCV library to read an image, convert it to grayscale, and apply gamma correction. Gamma correction is a non-linear adjustment to the intensity values of an image, often used to correct for the nonlinear relationship between pixel intensity and perceived brightness.

## Requirements
- Python 3
- OpenCV (`cv2`)
- NumPy
- Matplotlib

Install the required libraries using the following command:

```bash
pip install opencv-python numpy matplotlib
````

## Usage
1- Clone the repository to your local machine.
2- Make sure you have the required dependencies installed.
3- Replace the image path in the script with the path to your desired image.
4- Run the script using a Python interpreter:

```bash
python image_processing.py
```

## Functionality

**Display Original Image**
Reads an image from the specified file path.
Displays the original image.

**Convert to Grayscale**
Converts the original image to grayscale.
Displays the grayscale image.

**Histogram**
Computes and displays the histogram of the grayscale image.
Shows the distribution of pixel intensities.

**Gamma Correction**
Applies gamma correction to the grayscale image using both a look-up table (LUT) and manual pixel-wise modification.
Displays the gamma-corrected images.

**Execution Times**
Prints the execution times for gamma correction using a look-up table and manual pixel-wise modification.

**Histograms of Processed Images**
Displays histograms of the original image and the gamma-corrected images for visual comparison.

