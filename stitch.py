from PIL import Image

def stitch_images(images):
    # Ensure all images are opened
    opened_images = [Image.open(image) for image in images]

    # Assuming all images are of the same size
    img_width, img_height = opened_images[0].size

    # Create a new blank image to accommodate all images (2x2 grid)
    stitched_image = Image.new('RGB', (img_width * 2, img_height * 2))

    # Place each image onto the stitched image
    stitched_image.paste(opened_images[0], (0, 0))             # Top left
    stitched_image.paste(opened_images[1], (img_width, 0))     # Top right
    stitched_image.paste(opened_images[2], (0, img_height))    # Bottom left
    stitched_image.paste(opened_images[3], (img_width, img_height)) # Bottom right

    # Save the final image to the specified output path
    # stitched_image.save(output_path)
    return stitched_image

image_paths = ['icespice/0.png', 'icespice/1.png', 'icespice/2.png', 'icespice/0.png']

# Note: This code won't run here as it needs actual image files. You can run this code in your environment.
final_image = stitch_images(image_paths)
final_image.save("icespice/stiched.jpg")

# For demonstration purposes, you can uncomment this line if you run this in your environment.
# final_image.show()
