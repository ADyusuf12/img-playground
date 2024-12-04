import os
import sys
import argparse
import logging
from PIL import Image, ImageFilter, ImageEnhance

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def apply_filters(image_path, output_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        logging.info(f'Opened image: {image_path}')

        # Apply various filters
        img_sharpen = img.filter(ImageFilter.SHARPEN)
        img_blur = img.filter(ImageFilter.BLUR)
        img_detail = img.filter(ImageFilter.DETAIL)
        img_edges = img.filter(ImageFilter.FIND_EDGES)
        img_smooth = img.filter(ImageFilter.SMOOTH)

        # Enhance brightness, contrast, and color
        enhancer = ImageEnhance.Brightness(img)
        img_bright = enhancer.enhance(1.5)
        enhancer = ImageEnhance.Contrast(img)
        img_contrast = enhancer.enhance(1.5)
        enhancer = ImageEnhance.Color(img)
        img_color = enhancer.enhance(1.5)

        # Save all processed images
        filters = {
            'sharpen': img_sharpen,
            'blur': img_blur,
            'detail': img_detail,
            'edges': img_edges,
            'smooth': img_smooth,
            'bright': img_bright,
            'contrast': img_contrast,
            'color': img_color
        }

        if not os.path.exists(output_path):
            os.makedirs(output_path)
            logging.info(f'Created output directory: {output_path}')

        for filter_name, image in filters.items():
            output_file = os.path.join(output_path, f'{filter_name}_{os.path.basename(image_path)}')
            image.save(output_file)
            logging.info(f'Saved {filter_name} image to {output_file}')

        logging.info('All filters applied and images saved.')

    except Exception as e:
        logging.error(f'Error processing image: {e}')

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Apply various filters and enhancements to an image.')
    parser.add_argument('image_path', type=str, help='Path to the input image file')
    parser.add_argument('output_path', type=str, help='Directory to save the processed images')
    args = parser.parse_args()

    logging.info(f'Starting image processing: {args.image_path} -> {args.output_path}')
    apply_filters(args.image_path, args.output_path)

if __name__ == '__main__':
    main()
