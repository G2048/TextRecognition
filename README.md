# Tessaract Text Recognition

*This is a simple text recognition on based tesseract from google.*

**I have been created this a simple script  to recognize lecture code from youtube.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)


## Installation

To install the project, follow these steps:

1. You must install the [Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
2. Clone the repository.
3. Run `pip install -r requirements.txt` to install the dependencies.

## Usage

To use the project, run the following command:

```
 python.exe .\main.py -i .\tests\5.png
```

More Examples:
```
python.exe .\main.py -i .\tests\5.png --oem 3 --psm 6
python.exe .\main.py -i .\tests\0.png --language eng+rus
```

**Help:**
```
usage: main.py [-h] --image_path IMAGE_PATH [--to-pdf] [--window] [--language LANG] [--get-languages] [--blured] [--oem OEM] [--psm PSM] [--print-help-options]

options:
  -h, --help            show this help message and exit
  --image_path IMAGE_PATH, -i IMAGE_PATH
                        path to your image
  --to-pdf, -p          Convert image to pdf
  --window, -w          Print image to window
  --language LANG, -l   LANG Specify language
  --get-languages, -gl  List only available languages
  --blured, -b          Blur for preprocessing image
  --oem OEM, -o OEM     Specify OCR Engine mode
  --psm PSM, -psm PSM   Specify PSM
  --print-help-options, -pho Print help for --oem and --psm options
```

## Contributing

Contributions are welcome! Please follow the guidelines in CONTRIBUTING.md.

## License

This project is licensed under the MIT License. See LICENSE.txt for more information.