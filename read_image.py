from PIL import Image

def create_pixel_matrix(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to RGB (if not already in RGB, e.g., PNG with transparency)
    img = img.convert('RGB')
    
    # Get the size of the image
    width, height = img.size
    
    # Initialize the 2D list (matrix) to store pixel values
    pixel_matrix = []
    
    # Loop through each pixel in the image
    for y in range(height):
        row = []
        for x in range(width):
            # Get the RGB color of the pixel
            pixel = img.getpixel((x, y))
            row.append(pixel)
        pixel_matrix.append(row)
    
    return pixel_matrix

# Path to the image
image_path = r'C:\Users\minht\Downloads\color_picture.jpg'

# Create the 2D list of pixel values
pixel_matrix = create_pixel_matrix(image_path)

# For demonstration, print the first 10 rows
print(pixel_matrix[:10])