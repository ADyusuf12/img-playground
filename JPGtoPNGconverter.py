import os
import sys
from PIL import Image
import argparse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_jpg_to_png(image_folder, output_folder):
    # Check if the output folder exists, create if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        logging.info(f'Created output directory: {output_folder}')

    # Process each image in the input folder
    for filename in os.listdir(image_folder):
        try:
            if filename.endswith(".jpg") or filename.endswith(".jpeg"):
                img = Image.open(os.path.join(image_folder, filename))
                clean_name = os.path.splitext(filename)[0]
                img.save(os.path.join(output_folder, f'{clean_name}.png'), 'png')
                logging.info(f'Converted {filename} to PNG')
        except Exception as e:
            logging.error(f'Failed to process {filename}: {e}')
    
    logging.info('All conversions completed.')

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Convert JPG images to PNG format.')
    parser.add_argument('image_folder', type=str, help='Folder containing JPG images')
    parser.add_argument('output_folder', type=str, help='Folder to save PNG images')
    args = parser.parse_args()

    logging.info(f'Starting conversion: {args.image_folder} -> {args.output_folder}')
    convert_jpg_to_png(args.image_folder, args.output_folder)

if __name__ == '__main__':
    main()
