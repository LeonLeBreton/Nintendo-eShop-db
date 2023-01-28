from PIL import Image
import os

def concatenate_images(upper_image_path, lower_image_path, output_path):
    upper_image = Image.open(upper_image_path)
    lower_image = Image.open(lower_image_path)

    width, upper_height = upper_image.size
    _, lower_height = lower_image.size

    result_image = Image.new("RGB", (width, upper_height + lower_height))
    result_image.paste(upper_image, (0, 0))
    x = (width - lower_image.width) // 2
    y = upper_height
    result_image.paste(lower_image, (x, y))
    result_image.save(output_path)
    upper_image.close()
    lower_image.close() 
    os.remove(upper_image_path)
    os.remove(lower_image_path)
    
    