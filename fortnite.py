#This is the building block for the image capture with openCV for python

#import statements
import numpy as np
import cv2
from PIL import ImageGrab, Image
import os
import pytesseract


while True:
	img = ImageGrab.grab(bbox=[640,940, 690,970])
	img_np = np.array(img)

	frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
	#frame = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	#img to text right here my dude
	# write the grayscale image to disk as a temporary file so we can
	# apply OCR to it
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, frame)

	# load the image as a PIL/Pillow image, apply OCR, and then delete
	# the temporary file
	text = pytesseract.image_to_string(Image.open(filename))
	os.remove(filename)
	print(text)

	cv2.imshow("Screen", frame)

	if cv2.waitKey(1) == 27:
		break

cv2.destroyAllWindows()