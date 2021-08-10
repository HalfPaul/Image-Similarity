from PIL import Image
import numpy as np
import pywt
import warnings
warnings.filterwarnings("ignore")

# Wavelet hashing
class Whash:
    def __init__(self, image_dir):
        self.image = Image.open(image_dir)

    def compute_hash(self):
        '''Pixels of image are normalized and then we apply Discrete Wavelet Transform.
        Than the first row of coefficients is taken and we calculate the mean.
        Coefficients higher than mean are assigned 1 and others 0.''' 
        arr_image = np.asarray(self.image) / 255
        waves = pywt.wavedec2(arr_image, "haar", level=5)
        coefficients = waves[0]
        coeff_mean = np.mean(np.ndarray.flatten(coefficients))

        return (coefficients > coeff_mean).flatten()


    def check_similarity(self, another_phash, treshold=70):
        '''Hashes of both pictures are calculated and difference between count of 0s is taken.'''
        hash1 = self.compute_hash()
        hash2 = another_phash.compute_hash()
        difference = np.count_nonzero(hash1 != hash2)
        if difference < treshold:
            return True
        else:
            return False
        
        return False

    def __str__(self):
        bits = self.compute_hash()
        processed_bits = ''.join(str(b) for b in 1 * bits)
        hash = '{:0x}'.format(int(processed_bits, 2))
        return hash
    