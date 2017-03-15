import math
from PIL import Image
import numpy as np
import itertools

def evaluate_image(nn, image_location):
    image_flat = image_to_npflattened(image_location)
    print_image_flattened(image_flat)
    print nn.predict(image_flat)
    print nn.feedforward(image_flat)
    print 

def image_to_npflattened(image_location):
    im = Image.open(image_location)
    arr = np.asarray(im.getdata()).reshape(im.size[1], im.size[0], -1)
    arr_scaled = [1.0 - number / 255.0 for number in arr]
    arr_scaled = list(itertools.chain.from_iterable(arr_scaled))
    return np.array(arr_scaled)
    

def print_image_flattened(image):
    print_image_2d(image.reshape(int(math.sqrt(float(image.shape[0]))), int(math.sqrt(float(image.shape[0])))))

def print_image_2d(image):
    for row in range(image.shape[0]):
        nums = []
        for col in range(image.shape[1]):
            if image[row][col] == .0:
                nums.append('0')
            else:
                nums.append('1')
        print ''.join(nums)