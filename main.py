# You must have tesseract installation:
# https://github.com/UB-Mannheim/tesseract/wiki
# And you must have OpenCV installed

import argparse
import cv2
import pytesseract

# Set the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class OCR:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self._prepare_image()

    # Preprocess the image (e.g., convert to grayscale, apply thresholding, etc.)
    def _prepare_image(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        # thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        self.preprocessed_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # return thresholded

    def print_image(self):
        # Display the preprocessed image
        cv2.imshow("Preprocessed Image", self.preprocessed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def recognize_text(self, lang='eng', custom_config='--oem 3 --psm 6'):
        # Perform text recognition using pytesseract
        text = pytesseract.image_to_string(self.preprocessed_image, lang=lang, config=custom_config)
        return text

    def image_to_pdf(self):
        pdf = pytesseract.image_to_pdf_or_hocr(self.preprocessed_image, extension='pdf')
        with open('test.pdf', 'w+b') as f:
            f.write(pdf)  # pdf type is bytes by default


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', '-i', required=True, type=str, dest='image_path', help='path to your image')
    parser.add_argument('--to-pdf', '-p', action='store_true', dest='to_pdf', help='Convert image to pdf')
    parser.add_argument('--window', '-w', action='store_true', dest='window', help='Print image to window')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    parser = parse_args()
    image_path = parser.image_path

    ocr = OCR(image_path)
    recognized_text = ocr.recognize_text()
    print(recognized_text)

    if parser.to_pdf:
        ocr.image_to_pdf()
    if parser.window:
        ocr.print_image()