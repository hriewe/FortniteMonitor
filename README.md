# FortniteMonitor
Doing 'x' everytime you 'y' in Fortnite!

This code uses the python opencv library and the Tesseract OCR engine to monitor your health in the popular video game 'Fortnite'.

It is currrently skeleton code so that you can make it do whatever you want!
Ex. Texting me a funny joke every time my character dies in Fortnite :(
The code is well commented so you should have no problem adjusting it to your 'needs'! 
Enjoy!

## Setup

You will need python if you dont have it. Get it [here](https://www.python.org/downloads/)

Install the needed modules with:

`pip install Pillow`

`pip install opencv-python`

`pip install pytesseract`

You will need to download the Tesseract OCR engine for the code to run. On Mac, run `brew install tesseract`

For Windows users, click [here](https://github.com/tesseract-ocr/tesseract/wiki/Downloads) to download.

## How to run

Run the code with: `python fortnite.py`

Kill the program with: control-c

The code wont do much unless you tell it to. Some prior programming expierence is needed. Go over the code and look at the comments I have left and that will help you get started.

## Notes

Due to the nature of the Tesseract engine and just OCR technology in general, the code can be pretty buggy. If the OCR is failing to recognize your health play around with some PIL image processing. If you get the code working better than I have it, contribute! Just fork, edit, and open a pull request.

Also, the frames come in so fast that sometimes the code has a hard time removing them all from your directory. If you see some image files in the directory after running the code, just delete them.
