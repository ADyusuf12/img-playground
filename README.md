# Image Playground

## Introduction
**Image Playground** is a Python project designed to handle various image processing tasks. Currently, it includes:
- A script to convert JPG images to PNG format.
- A script to apply multiple filters and enhancements to images.

## Features
### JPG to PNG Converter
- **Convert JPG to PNG:** Easily convert your JPG images to PNG format.
- **Error Handling:** Gracefully handles errors and provides informative messages.
- **Progress Reporting:** Outputs conversion progress to the console.
- **Command-Line Arguments:** Uses `argparse` for flexible input and output folder specifications.
- **Logging:** Detailed logging of the conversion process.

### Image Filter and Enhancement
- **Apply Filters:** Applies various filters like SHARPEN, BLUR, DETAIL, FIND_EDGES, and SMOOTH.
- **Enhance Image:** Enhances brightness, contrast, and color.
- **Command-Line Arguments:** Specify the image file and output directory via command-line arguments.
- **Logging:** Logs the steps performed for better traceability.

## Technologies Used
- **Python**
- **Pillow (PIL Fork):** Image processing library

## Installation Instructions
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/image-playground.git
   cd image-playground
