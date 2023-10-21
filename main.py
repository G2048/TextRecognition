# You must have tesseract installation:
# https://github.com/UB-Mannheim/tesseract/wiki
# And you must have OpenCV installed
#

import os
import argparse
import cv2
import pytesseract

# Set the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def recognize_text(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Preprocess the image (e.g., convert to grayscale, apply thresholding, etc.)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    # thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Display the preprocessed image
    preprocessed_image = thresholded
    cv2.imshow("Preprocessed Image", preprocessed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Perform text recognition using pytesseract
    text = pytesseract.image_to_string(thresholded)

    return text


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', '-i', required=True, type=str, dest='image_path', help='path to your image')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    parser = parse_args()
    image_path = os.getcwd() + parser.image_path.strip('.')

    recognized_text = recognize_text(image_path)
    print(recognized_text)
