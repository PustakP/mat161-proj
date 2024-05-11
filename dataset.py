from PIL import Image
import shutil
import os
from thispersondoesnotexist import get_online_person #imports


for i in range(1600):
    picture = get_online_person()  # bytes representation of the image

    # Save to a file

    print("Saving picture...", i, end="\r")

    from thispersondoesnotexist import save_picture


    save_picture(picture, str(i)+".jpeg") # saves image to file

    # Open the image
    image_path = str(i) + ".jpeg"
    image = Image.open(image_path)

    # Rescale the image to 100x100
    rescaled_image = image.resize((100, 100))

    # Convert the image to grayscale
    grayscale_image = rescaled_image.convert("L")

    # Save the grayscale image
    grayscale_image.save(image_path)

    # Move the image to the faces subfolder
    shutil.move(image_path, "faces/" + image_path)
    


