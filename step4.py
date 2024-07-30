#Beautifying

from PIL import Image

# Load the two images
image1 = Image.open('FieldDiagram.png')
image2 = Image.open('homo1.png')

# Resize image2 to match the size of image1
image2 = image2.resize(image1.size)

# Create a new image with the same size as image1
merged_image = Image.new('RGB', image1.size)

# Set the weight for image1 (between 0 and 1)
weight = 0.7

# Blend the images together
merged_image = Image.blend(image1, image2, weight)

# Save the merged image
merged_image.save('mergedfinal.jpg')