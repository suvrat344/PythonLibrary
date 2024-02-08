from PIL import Image,ImageFilter,ImageFont,ImageDraw,ImageEnhance
import matplotlib.pyplot as plt
import numpy as np
import os


# Open Image
image1 = Image.open("img1.jpg")
image2 = Image.open("img2.jpg")


# Image Properties
print("Size : ",image1.size)
print("Format : ",image1.format)
print("Mode : ",image1.mode)


# Crop Image
left,top,right,bottom = 50,120,250,230
crop_image = image1.crop((left,top,right,bottom))
plt.imshow(crop_image)
plt.show()


# Copy Image
copied_image = image1.copy()
plt.imshow(copied_image)
plt.show()


# Transposing Image
image1.rotate(180)
transpose_image1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
transpose_image2 = image1.transpose(Image.FLIP_TOP_BOTTOM)
transpose_image3 = image1.transpose(Image.ROTATE_90)
transpose_image4 = image1.transpose(Image.ROTATE_180)
transpose_image5 = image1.transpose(Image.ROTATE_270)
transpose_image6 = image1.transpose(Image.TRANSPOSE)
plt.figure(figsize=(10,10))
plt.subplot(3,2,1)
plt.imshow(transpose_image1)
plt.title("FLIP_LEFT_RIGHT")
plt.subplot(3,2,2)
plt.imshow(transpose_image2)
plt.title("FLIP_TOP_BOTTOM")
plt.subplot(3,2,3)
plt.imshow(transpose_image3)
plt.title("ROTATE_90")
plt.subplot(3,2,4)
plt.imshow(transpose_image4)
plt.title("ROTATE_180")
plt.subplot(3,2,5)
plt.imshow(transpose_image5)
plt.title("ROTATE_270")
plt.subplot(3,2,6)
plt.imshow(transpose_image6)
plt.title("TRANSPOSE")
plt.show()


# Resize Image
new_size = (300,300)
plt.figure(figsize=(10,10))
resized_image1 = image1.resize(new_size,Image.BILINEAR)
resized_image2 = image1.resize(new_size,Image.NEAREST)
resized_image3 = image1.resize(new_size,Image.BOX)
resized_image4 = image1.resize(new_size,Image.HAMMING)
resized_image5 = image1.resize(new_size,Image.BICUBIC)
resized_image6 = image1.resize(new_size,Image.LANCZOS)
plt.subplot(3,2,1)
plt.imshow(resized_image1)
plt.title("BILINEAR")
plt.subplot(3,2,2)
plt.imshow(resized_image2)
plt.title("NEAREST")
plt.subplot(3,2,3)
plt.imshow(resized_image3)
plt.title("BOX")
plt.subplot(3,2,4)
plt.imshow(resized_image4)
plt.title("HAMMING")
plt.subplot(3,2,5)
plt.imshow(resized_image5)
plt.title("BICUBIC")
plt.subplot(3,2,6)
plt.imshow(resized_image6)
plt.title("LANCZOS")
plt.show()


# Rotating Image
angle1 = 30
rotated_image = image1.rotate(angle1)
plt.imshow(rotated_image)
plt.show()

angle2 = -30
rotated_image = image1.rotate(angle2)
plt.imshow(rotated_image)
plt.show()


# Text WaterMark
watermarked_image = image1.copy()
draw = ImageDraw.Draw(watermarked_image)
font = ImageFont.truetype("arial.ttf",100)
draw.text((0,0),'Sample Text',(0,0,0),font=font)
draw.text((0,0),'Sample Text',(255,255,255),font=font)
plt.imshow(watermarked_image)
plt.show()


# Image WaterMark
size = (500,500)
crop_image = image1.copy()
crop_image.thumbnail(size)             # Preserve Aspect Ratio
copied_image = image1.copy()
copied_image.paste(crop_image,(0,0))
plt.imshow(copied_image)
plt.show()


# Convert Into Black And White
bw_image = image1.convert(mode="L") 
plt.imshow(bw_image,cmap="gray")    # use cmap gray for matplotlib to correctly show black and white
plt.show()


# Convert To Different Formats
new_format_image = image1.convert("HSV") 
print(new_format_image.mode)


# Convert To Numpy Formats
numpy_array = np.array(image1) 
print(numpy_array.shape)
numpy_image = Image.fromarray(numpy_array)
plt.imshow(numpy_image)
plt.show()


# Image Enhancement
image_color_enhance = image1.copy()
plt.figure(figsize=(10,10))
image11 = ImageEnhance.Color(image_color_enhance).enhance(2.5)
image12 = ImageEnhance.Contrast(image_color_enhance).enhance(2.5)
image13 = ImageEnhance.Brightness(image_color_enhance).enhance(1.5)
image14 = ImageEnhance.Sharpness(image_color_enhance).enhance(2.5)
plt.subplot(2,2,1)
plt.imshow(image11)
plt.title("Color")
plt.subplot(2,2,2)
plt.imshow(image12)
plt.title("Contrast")
plt.subplot(2,2,3)
plt.imshow(image13)
plt.title("Brightness")
plt.subplot(2,2,4)
plt.imshow(image14)
plt.title("Sharpness")
plt.show()


# Alpha Blending => Mixing Of Two Image
image11 = image1.copy()
image12 = image2.copy()
image12 = image12.resize(image11.size)
image_blend = Image.blend(image11,image12,0.5)
plt.imshow(image_blend)
plt.show()


# ImageTransform
image_transform = image1.copy()
image_transform = image_transform.transform(image_transform.size,Image.AFFINE,(1,-0.5,0.5*image_transform.size[0],0,1,0))
plt.imshow(image_transform)
plt.show()

image_transform = image1.copy()
image_transform = image_transform.transform(image_transform.size,Image.EXTENT,(100,100,image_transform.size[0],image_transform.size[1]//2))
plt.imshow(image_transform)
plt.show()


# Flipping Channel
image_channel = image1.copy()
r,g,b = image_channel.split()
im = Image.merge("RGB",(b,g,r))
plt.imshow(im)
plt.show()


# # Blur Image
image1 = Image.open("img1.jpg")
image1.filter(ImageFilter.GaussianBlur(15)).save("img13.png")


# Save Image
image1.save("newImage.jpg")


# Display Image
image1.show()


size_300 = (300,300)
size_700 = (700,700)
for f in os.listdir("."):
    if(f.endswith('.jpg')):
        i = Image.open(f)                             # Open Image
        fn,fext = os.path.splitext(f)                 # Split file with extension
        i.save('pngs/{}.png'.format(fn))              # Save Image as PNG Image 

        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn,fext))

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn,fext))