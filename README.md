![Image_Processing_with_Gamma_Correction_!](https://github.com/BaraSedih11/ImageHW1/assets/98843912/7417fe86-11a0-46b9-866e-7172ba99febb)

  ![GitHub repo size](https://img.shields.io/github/repo-size/BaraSedih11/ImageHW1) ![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/BaraSedih11/ImageHW1)  ![NPM Version](https://img.shields.io/npm/v/npm)




## Overview
This project demonstrates basic image processing techniques, focusing on gamma correction. The script utilizes the OpenCV library to read an image, convert it to grayscale, and apply gamma correction. Gamma correction is a non-linear adjustment to the intensity values of an image, often used to correct for the nonlinear relationship between pixel intensity and perceived brightness.

## Requirements
- Python 3
- OpenCV (`cv2`)
- NumPy
- Matplotlib

Install the required libraries using the following command:

![image](https://github.com/BaraSedih11/ImageHW1/assets/98843912/8f7212b4-0e60-4e6c-90ad-0bd4196217f6)

## Usage
<iframe
  src="https://carbon.now.sh/embed?bg=rgba%28171%2C+184%2C+195%2C+1%29&t=seti&wt=none&l=python&width=680&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false&code=import%2520cv2%2520as%2520cv%250Aimport%2520numpy%2520as%2520np%250Aimport%2520matplotlib.pyplot%2520as%2520plt%250Aimport%2520time"
  style="width: 1024px; height: 473px; border:0; transform: scale(1); overflow:hidden;"
  sandbox="allow-scripts allow-same-origin">
</iframe>

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

