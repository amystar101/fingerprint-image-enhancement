# Fingerprint Image Enhancement

Python implementation for enhancing the fingerprint images

orignal Image
![Alt text](./src/input_images/input.bmp)
<br />
Enhanced Image
![Alt text](./src/output_images/output.png)
<br />
image used from kaggle (Fingerprint Image Dataset from FVC2000_DB4_B)
<br />
link - https://www.kaggle.com/peace1019/fingerprint-dataset-for-fvc2000-db4-b
## Files

### main.py
Driver file that connects other files

### normalise.py
Python file for normalising the input image
<br />
Inputs - image, new mean(default = 1), new variance(default = 1)
<br />
Output - return the normalised image with mean = new mean and variance = new variance

### gradient.py
operate the sobel operator on the given input image
<br />
Input = Image
<br />
output = Images after the sobel operation along horizontal axis and vertical axis

### orientation.py
for calculating the orientation in the fingerprint image
<br />
Inputs = Image , filter size w (default = 16)
<br />
Output = calculated orientation of image

### ridge_frequency.py
for calculating the ridge frequency in image
<br />
Inputs = image, orientation, w (default = 2), mnlambda (default = 3), mxlambda(default = 15)
<br />
output - ridge frequency of the image

### gabor_filter.py
apllies the gabor filter
<br />
Input = Image, frequency, orientation
<br />
Output = Enhanced Image

## Workflow

<ol>
<li>Image is firstly padded with certain width along all the flour directrion.</li>
<li>Image is normalised with new mean and variance equal to 1.</li>
<li>Normalised image is passed with low pass filter to reduce the effect of sudden change in pixel values.</li>
<li>Orientation in image is calculated using simple sobel filter.</li>
<li>Ridge frequency is calculated using the orientation.</li>
<li>Simple interpolation method is used for finding the frequency values at some location.</li>
<li>Gabor filter is applied.</li>
</ol>

## Usage
<ul>
<li>Place the image in input folder.</li>
<li>change the name variable in main file (line 12) with the name of the image file(complete with exetension). </li>
<li>Execute python3 main.py in terminal window.<li>
<li>press 0 to continue from image progress preview.</li>
<li>save the final enhanced image.<li>
</ul>
