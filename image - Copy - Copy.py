from PIL import Image
 
#read the image from path
image = Image.open(r"D:\Prayag Files\Coding\Python\Projects\Black n white image processing\display\ips.jpg") 
 
#Convert it into the grayscale image
grayscale = image.convert('L')
 
#Converting the same image to black and white mode
BW= image.convert('1')
 
#save both the images
grayscale.save("grayscale_image.jpg")
BW.save("BW_image.jpg")