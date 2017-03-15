from PIL import Image

#'C:/Users/VSZM5/Desktop/handwritten_digits.jpg'

# returns a list of triplets containing rgb color info for each pixel as integers
def load_flattened_greyscale_pixels_from_jpg(file_location):
    im = Image.open(file_location)
    im = im.convert('L')
    im.show()
    im.save('C:/Users/VSZM5/git/neural-networks-and-deep-learning/greyscaled.jpg')
    return [val / 255.0 for val in im.getdata()]


segment:
http://scikit-image.org/docs/dev/auto_examples/segmentation/plot_label.html#sphx-glr-auto-examples-segmentation-plot-label-py
http://scikit-image.org/docs/dev/auto_examples/xx_applications/plot_coins_segmentation.html#sphx-glr-auto-examples-xx-applications-plot-coins-segmentation-py
http://scikit-image.org/docs/dev/auto_examples/segmentation/plot_watershed.html#sphx-glr-auto-examples-segmentation-plot-watershed-py
