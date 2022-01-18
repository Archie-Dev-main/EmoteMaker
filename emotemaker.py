import installer

install = installer.Installer()
install.install_required_modules()

from PIL import Image
import os
import sys

class EmoteMaker:
    def __init__(self, input_dir, output_dir):
        # Quick, generic way of storing the parameters for use in the rest of the code
        self.dirs = [input_dir, output_dir]
        # To store all of the images that are over 256 kb
        self.overwieght_images = []

        # Builds the list of overweight files to be modified
        for filename in os.listdir(input_dir):
            f = os.path.join(input_dir, filename)

            if os.path.getsize(f) > (256 * 1024):
                self.overwieght_images.append(f)
    
    def fix_overweight_image(self, image_dir):
        print(os.path.basename(image_dir))
        image = Image.open(image_dir)

        image_compressed = image.quantize(method=2)

        image_compressed.save(self.dirs[1] + "\\" + os.path.basename(image_dir))
    
    def fix_all_images(self):
        for i in self.overwieght_images:
            self.fix_overweight_image(i)

input_dir = "C:\\Users\\Colten\\Pictures\\certified_nick_faces\\to_be_converted"
output_dir = "C:\\Users\\Colten\\Pictures\\certified_nick_faces\\emotes"
test = EmoteMaker(input_dir, output_dir)
test.fix_all_images()

test_file = open("list.txt", 'w')
for i in test.overwieght_images:
    test_file.write(i + "\n")
