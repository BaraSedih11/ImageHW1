import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time



#my img --------------(1)
img = cv.imread('images/Sunset.jpg')
cv.imshow('Sunset', img)

#gray------------------(2)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



#histogram-----------------(3)
hist = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.xlabel('Intensity')
plt.ylabel('Count Of Pixels')
plt.xlim([0, 256])
plt.locator_params(axis='x', nbins=50)
plt.plot(hist)
plt.show()


#gamma  --------------(4)
gamma = 2

# Using look-up table
start_time_lut = time.time()
gamma_table = np.array([((i / 255.0) ** (1 / gamma)) * 255 for i in np.arange(0, 256)]).astype("uint8")
img_gamma_corrected_lut = cv.LUT(img, gamma_table)
end_time_lut = time.time()
time_taken_lut = end_time_lut - start_time_lut

# By modifying each pixel individually
start_time_manual = time.time()
img_gamma_corrected_manual = np.power((img / 255.0), (1.0 / gamma))
img_gamma_corrected_manual = np.uint8(img_gamma_corrected_manual * 255)
end_time_manual = time.time()
time_taken_manual = end_time_manual - start_time_manual

cv.imshow("Gamma Corrected Image (Using Look-Up Table)", img_gamma_corrected_lut)
cv.imshow("Gamma Corrected Image (Manual)", img_gamma_corrected_manual)

# Display the execution times---------------(5)
print("Time taken using look-up table: {:.6f} seconds".format(time_taken_lut))
print("Time taken manually: {:.6f} seconds".format(time_taken_manual))



# Plot the histograms ---------------(6)
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.hist(img.ravel(), 256, [0, 256])
plt.title("The Original Image")

plt.subplot(2, 2, 2)
plt.hist(img_gamma_corrected_lut.ravel(), 256, [0, 256])
plt.title("Gamma Corrected Image (Using Look-Up Table)")

plt.subplot(2, 2, 3)
plt.hist(img_gamma_corrected_manual.ravel(), 256, [0, 256])
plt.title("Gamma Corrected Image (Manual)")

plt.show()




cv.waitKey(0)
