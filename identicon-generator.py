import customidenticon
import hashlib
from random import randint
import os


identicon_types = ['layers', 'pixels', 'blocks']
for identicon_type in identicon_types:
    print(identicon_type)
    for i in range(1,101):
        #max range is 2-5 for blocks
        #5-10 is for pixels & layers
        if identicon_type == 'layers':
            range_low = 5
            range_high = 11
        elif identicon_type == 'pixels':
            range_low = 5
            range_high = 11
        elif identicon_type == 'blocks':
            range_low = 2
            range_high = 5
        for pixel_count in range(range_low, range_high):
                identicon = customidenticon.create(
                    "Test data",                # Data
                    type=identicon_type,        # Type of algorithm (pixels, blocks or layers)
                    salt=str(i*3.14),           # salt for more variants
                    background="#f0f0f0",       # background color
                    block_visibility=140,       # transparency of elements in the image (0-255)
                    block_size=30,              # size of elements (px)
                    border=25,                  # border (px)
                    size=pixel_count,           # number of elements
                    hash_func=hashlib.sha512    # hash function (auto)
                )
                name = f"{identicon_type}-{str(pixel_count)}-{str(i)}.jpg"
                
                save_path = f"identicons\\{identicon_type}\\{str(pixel_count)}"
                full_name = os.path.join(save_path, name)
                
                f = open(full_name, "wb")
                f.write(identicon)

