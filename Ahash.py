from PIL import Image
import numpy as np


#Average hashing
class Ahash:
    def __init__(self, image_dir):
        self.image = Image.open(image_dir)
    
    def compute_hash(self):
        '''The image is resized to 8x8 and greyscaled. Then the mean of image is calculated
        and pixels higher than mean are turned into 1 and everything else into 0.'''
        processed_image = self.image.resize((8, 8)).convert('L')
        arr_image = np.asarray(processed_image)
        image_mean = np.mean(arr_image)
        return (arr_image > image_mean).flatten()

    def check_similarity(self, another_ahash, treshold=10):
        '''Hashes of both pictures are calculated and difference between count of 0s is taken.'''
        diff1 = self.compute_hash()
        diff2 = another_ahash.compute_hash()
        difference = np.count_nonzero(diff1 != diff2)
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
