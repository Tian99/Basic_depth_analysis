from PIL import Image

def rotate(image_path, degrees_to_rotate, saved_location):
    """
    Rotate the given photo the amount of given degreesk, show it and save it
    @param image_path: The path to the image to edit
    @param degrees_to_rotate: The number of degrees to rotate the image
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    rotated_image = image_obj.rotate(degrees_to_rotate)
    rotated_image = rotated_image.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(saved_location)

# rotate('output/ps2-3-a-2.bmp', 0, 'output/ps2-3-a-2.bmp')