from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

opt_size = [28, 28]

#Check image and saves as variable
try:
    #Saves preset image on computer as the user image
    user_img = Image.open('/Users/liamkehoe/Downloads/brainfeeder_beeple-vjclips/hello.jpg')
except IOError:
    pass

#Checks to see if image is correct size, and if not, shrinks it down to the correct size
if user_img.size[0] == opt_size[0] & user_img.size[1] == opt_size[1]:
    print('Image is already 28 x 28')
else:
    processed_img = user_img.resize([28, 28])

#Create the plot to display the images
plt.figure()

f, axarr = plt.subplots(2,1)

axarr[0].imshow(user_img)
axarr[1].imshow(processed_img)

plt.axis('off')
plt.show()
