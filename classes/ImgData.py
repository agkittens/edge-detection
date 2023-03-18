from SobelsMasks import Sobel
from PIL import Image
import itertools

class Img:
    def __init__(self, image, imageCopy):
        self.width = image.width - 4
        self.height = image.height - 4
        self.pixelsValues = imageCopy.load()
        self.pixels = image.load()

    def masking(self):
        for pixelH, pixelW in itertools.product(range(self.height), range(self.width)):
            for maskNum in range(4):
                rgbColor = [[0]*3]*4
                r,g,b = 0, 0, 0

                for colorNum in range(3):
                    for y in range(9):
                        rgbColor[maskNum][colorNum] += (self.pixelsValues[pixelW + y%3, pixelH+y//3][colorNum]*Sobel.masks[maskNum][y])

                    if (rgbColor[maskNum][colorNum]<0): rgbColor[maskNum][colorNum]=abs(rgbColor[maskNum][colorNum])
                    if (rgbColor[maskNum][colorNum]>255): rgbColor[maskNum][colorNum]=255

                r += rgbColor[maskNum][0]
                g += rgbColor[maskNum][1]
                b += rgbColor[maskNum][2]

            self.pixels[pixelW+1, pixelH+1] = (r, g, b)

    def loadingPixels(self,image):
        imageTransformed = Image.new(mode = 'RGB', size = (self.width, self.height))

        for pixelH, pixelW in itertools.product(range(self.height-4), range(self.width-4)):
            imageTransformed.putpixel((pixelW+1, pixelH+1),self.pixels[pixelW+1, pixelH+1])

        imageTransformed.save('sobel.png')
        imageTransformed.close()
