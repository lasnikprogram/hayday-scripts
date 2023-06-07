#!/usr/bin/env python3

from bs4 import BeautifulSoup
from argparse import ArgumentParser
import requests
import os
import numpy as np
from PIL import Image

parser = ArgumentParser(description='scrape images for HayDay products from hayday.fandom.com')
parser.add_argument('--small', type=bool, default=True,
                    help='whether or not to make the url smaller')
parser.add_argument('--download', type=bool, default=False,
                    help='whether or not to download the images')
parser.add_argument('--alpha', type=bool, default=True,
                    help='whether ot not to convert pixels with zero opacity to\
                    the rgba value (0,0,0,0) (useful for further image processing and recognition)')
parser.add_argument('--location', type=str, default='icons',
                    help='location to download the images to')
parser.add_argument('--seperator', type=str, default=', ',
                    help='character to use when seperating name and image url in the output')

args = parser.parse_args()

getURL = requests.get('https://hayday.fandom.com/wiki/Products')
soup = BeautifulSoup(getURL.text, 'html.parser')

table_body = soup.find('tbody')
rows = table_body.find_all('tr')

images, names = [], []

for row in rows:
    containers = row.find_all('td')
    for container in containers:
        image = container.find('img')
        name = container.find('b')

        if image:
            image_url = image.get('data-src')
            if not image_url:
                image_url = image.get('src')

            if args.small:
                image_url = image_url.split('.png')[0] + '.png'

            images.append(image_url)
        elif name:
            name = name.find('a')
            if name:
                names.append(name.get('title'))

# TODO: multiprocessing; if file already present: skip; don't use the wiki at all

for i in range(len(images)):
    print(names[i], images[i], sep=args.seperator)
    if args.download:
        if not os.path.exists(args.location):
            os.makedirs(args.location)

        image = requests.get(images[i]).content
        file_location = f'{args.location}/{names[i]}.png'
        with open(file_location, 'wb') as handler:
            handler.write(image)

        if args.alpha:
            image = Image.open(file_location)
            np_image = np.array(image)
            alpha_channel = np_image[:, :, 3]
            zero_alpha_indices = np.where(alpha_channel == 0)
            np_image[zero_alpha_indices] = [0, 0, 0, 0]

            image = Image.fromarray(np_image)
            image.save(file_location)
            image.close()



