from PIL import Image
from ImgData import Img

def main():
    print('enter image path: ')
    filePath = input()

    try: Image.open(filePath)
    except: print('invalid path')

    with Image.open(filePath, 'r') as image:
        imageCopy = Image.open(filePath, 'r')
        imageData = Img(image,imageCopy)
        imageData.masking()
        imageData.loadingPixels()
        print('saved')
        image.close()

main()
