# You must have tesseract installated:
# https://github.com/UB-Mannheim/tesseract/wiki
# And you must have OpenCV installed

import argparse
import cv2
import pytesseract

# Set the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class OCR:
    def __init__(self, image_path, blure=False):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self._prepare_image(blure)

    # Preprocess the image (e.g., convert to grayscale, apply thresholding, etc.)
    def _prepare_image(self, blure):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        if blure:
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            self.preprocessed_image = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        else:
            self.preprocessed_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    def print_image(self):
        # Display the preprocessed image
        cv2.imshow("Preprocessed Image", self.preprocessed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # For more information about tessaract options, see:
    # https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc

    def recognize_text(self, lang='eng', oem='3', psm='6'):
        custom_config = f'--oem {oem} --psm {psm}'
        # Perform text recognition using pytesseract
        text = pytesseract.image_to_string(self.preprocessed_image, lang=lang, config=custom_config)
        return text

    def image_to_pdf(self):
        pdf = pytesseract.image_to_pdf_or_hocr(self.preprocessed_image, extension='pdf')
        with open('test.pdf', 'w+b') as f:
            f.write(pdf)  # pdf type is bytes by default

def print_help_options():
    help_options = """
     --psm N
         Set Tesseract to only run a subset of layout analysis and assume a certain form of image. The options for N are:
         ```
         0 = Orientation and script detection (OSD) only.
         1 = Automatic page segmentation with OSD.
         2 = Automatic page segmentation, but no OSD, or OCR. (not implemented)
         3 = Fully automatic page segmentation, but no OSD. (Default)
         4 = Assume a single column of text of variable sizes.
         5 = Assume a single uniform block of vertically aligned text.
         6 = Assume a single uniform block of text.
         7 = Treat the image as a single text line.
         8 = Treat the image as a single word.
         9 = Treat the image as a single word in a circle.
         10 = Treat the image as a single character.
         11 = Sparse text. Find as much text as possible in no particular order.
         12 = Sparse text with OSD.
         13 = Raw line. Treat the image as a single text line,
              bypassing hacks that are Tesseract-specific.
         ```

         --oem N
         Specify OCR Engine mode. The options for N are:
         ```
         0 = Original Tesseract only.
         1 = Neural nets LSTM only.
         2 = Tesseract + LSTM.
         3 = Default, based on what is available.
         ```
         
    For more information about tessaract options, see:
    https://github.com/tesseract-ocr/tesseract/blob/main/doc/tesseract.1.asc
         
     """
    print(help_options)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', '-i', required=True, type=str, dest='image_path', help='path to your image')
    parser.add_argument('--to-pdf', '-p', action='store_true', dest='to_pdf', help='Convert image to pdf')
    parser.add_argument('--window', '-w', action='store_true', dest='window', help='Print image to window')
    parser.add_argument('--language', '-l', action='store', default='eng', dest='lang', help='Specify language')
    parser.add_argument('--get-languages', '-gl', action='store_true', dest='list_lang', help='List only available languages')
    parser.add_argument('--blured', '-b', action='store_true', default=False, dest='blure', help='Blur for preprocessing image')
    parser.add_argument('--oem', '-o', action='store', default='3', dest='oem', help='Specify OCR Engine mode')
    parser.add_argument('--psm', '-psm', action='store', default='6', dest='psm', help='Specify PSM')
    parser.add_argument('--print-help-options', '-pho', action='store_true', dest='print_help_options', help='Print help for --oem and --psm options')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    parser = parse_args()
    image_path = parser.image_path

    if parser.list_lang:
        print(pytesseract.get_languages())
        exit()
    elif parser.print_help_options:
        print_help_options()
        exit()

    ocr = OCR(image_path, parser.blure)
    recognized_text = ocr.recognize_text(parser.lang, parser.oem, parser.psm)
    print(recognized_text)

    if parser.to_pdf:
        ocr.image_to_pdf()
    if parser.window:
        ocr.print_image()