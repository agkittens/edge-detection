from SobelsMasks import Sobel
from PIL import Image

class Img:
    def __init__(self, image, imageCopy):
        self.width = image.width
        self.height = image.height
        self.pixelsValues = imageCopy.load()
        self.pixels = image.load()

    def masking(self):
        for pixelH in range(self.height-4):
            for pixelW in range(self.width-4):
                for maskNum in range(4):
                    rgbColor = [[0]*3]*4
                    r,g,b = 0, 0, 0

                    for colorNum in range(3):
                        for y in range(3):
                            rgbColor[maskNum][colorNum] += (self.pixelsValues[pixelW, pixelH+y][colorNum]*Sobel.masks[maskNum][3*y]+self.pixelsValues[pixelW+1, pixelH+y][colorNum]*Sobel.masks[maskNum][1+3*y]+self.pixelsValues[pixelW+2,pixelH+y][colorNum]*Sobel.masks[maskNum][2+3*y])

                        if (rgbColor[maskNum][colorNum]<0): rgbColor[maskNum][colorNum]=abs(rgbColor[maskNum][colorNum])
                        if (rgbColor[maskNum][colorNum]>255): rgbColor[maskNum][colorNum]=255

                    r += rgbColor[maskNum][0]
                    g += rgbColor[maskNum][1]
                    b += rgbColor[maskNum][2]

                self.pixels[pixelW+1, pixelH+1] = (r, g, b)

    def loadingPixels(self,image):
        imageTransformed = Image.new(mode = 'RGB', size = (self.width, self.height))

        for pixelH in range(self.height-4):
            for pixelW in range(self.width-4):
                imageTransformed.putpixel((pixelW+1, pixelH+1),self.pixels[pixelW+1, pixelH+1])

        imageTransformed.save('sobel.png')
        imageTransformed.close()
