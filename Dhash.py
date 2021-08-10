from PIL import Image
import numpy as np


#Difference hashing
class Dhash:
    def __init__(self, image_dir):
        self.image = Image.open(image_dir)


    def compute_difference(self):
        '''Image is resized to 9x8 and converted to grayscale, then we calculate the difference between columns.'''
        processed_image = self.image.resize((9, 8)).convert('L')
        arr_image = np.asarray(processed_image)
        difference = arr_image[:, 1:] > arr_image[:, :-1]
        return difference
    
    def check_similarity(self, another_phash, treshold=10):
        '''Hashes of both pictures are calculated and difference between count of 0s is taken.'''
        diff1 = self.compute_difference()
        diff2 = another_phash.compute_difference()
        difference = np.count_nonzero(diff1 != diff2)
        if difference < treshold:
            return True
        else:
            return False
        return False

    def __str__(self):
        bits = self.compute_difference()
        processed_bits = ''.join(str(b) for b in 1 * bits)
        hash = '{:0x}'.format(int(processed_bits, 2))
        return hash
