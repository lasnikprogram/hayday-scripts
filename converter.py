#!/usr/bin/python3
import os
from PIL import Image
import numpy as np

# helps PIL with template matching by providing "true" zero opacity pixels in images (prevent artifacts)
image_directory = 'images/'

# Get a list of image files in the directory
image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]

for image_file in image_files:
    image_path = os.path.join(image_directory, image_file)
    print(f'opening {image_path}')
    image = Image.open(image_path)

    np_image = np.array(image)
    alpha_channel = np_image[:, :, 3]
    zero_alpha_indices = np.where(alpha_channel == 0)
    np_image[zero_alpha_indices] = [0, 0, 0, 0]

    image = Image.fromarray(np_image)
    image.save(image_path)
    image.close()
    print(f'{image_path} done')

