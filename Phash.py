from PIL import Image
import numpy as np
from scipy.fft import dct

# Perceptual Hashing
class Phash:
    def __init__(self, image_dir):
        self.image = Image.open(image_dir)

    def compute_hash(self):
        '''The image is resized and converted to grayscale,
        then Discrete Cosine Transform(dct) is applied and top 8x8 coefficients are taken,
        then the mean of values is calculated and coefficients higher than the mean turns
        into 1 and everything else into 0.''' 
        processed_image = self.image.resize((32, 32)).convert('L')
        arr_image = np.asarray(processed_image)
        dct_image = dct(dct(arr_image, axis=0), axis=1)[:8,:8]
        image_mean = np.mean(dct_image)
        return (dct_image > image_mean).flatten()


    def check_similarity(self, another_phash, treshold=10):
        '''Hashes of both pictures are calculated and difference between count of 0s is taken.
        Difference treshold of 10 is what I found to be best performing.'''
        hash1 = self.compute_hash()
        hash2 = another_phash.compute_hash()
        difference = np.count_nonzero(hash1 != hash2)
        if difference < treshold:
            return True
        else:
            return False
        return False

    def __str__(self):
        "The ones and zeros are converted to hexadecimal number."
        bits = self.compute_hash()
        processed_bits = ''.join(str(b) for b in 1 * bits)
        hash = '{:0x}'.format(int(processed_bits, 2))
        return hash


