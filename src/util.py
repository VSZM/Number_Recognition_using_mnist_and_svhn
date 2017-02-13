import math

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