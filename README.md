# hayday-scripts
Some scripts I used to get a statistical overview of items sold in the hayday paper. The database I aquired is private for now but you can easily built your own one using these scripts.

## scripts
### product-image-scraper.py
Used to download images and names for all items using the forum.  
Run `python3 product-image-scraper.py -h` to see the usage.

### converter.py
Convert images which would normally render artifacts when used in OpenCV to clear images by fixing some alpha properties.  
__This can also be used outside of the HayDay scope if you encounter artifacts when reading images with OpenCV!__  
You have to specify a folder inside the script to use it.

### text.py
Get each product from a screenshot of the Hayday paper as a string.

## notice
I am not publishing any assets from any Supercell game. The only thing I am using is the term "Hay Day". So just to ensure clarity:  
_This material is unofficial and is not endorsed by Supercell. For more information see Supercell's Fan Content Policy: www.supercell.com/fan-content-policy._
