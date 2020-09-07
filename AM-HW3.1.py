from PIL import Image,ImageDraw
from SortFunctions import binarySearchSub,selectionSort,recurSelectionSort,quickSortIterative


def comparePixels(pix1, pix2):
    return pix1[0][0] > pix2[0][0]

def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])
    pixel_array=[]
    for i in range (width):
        for j in range(height):
            r,g,b = im.getpixel((i,j))
            pixel_array.append([(r,g,b),(i,j)])
    return pixel_array


def pixelsToImage(im, pixels):
    outimg = Image.new("RGB",im.size);
    outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg
def pixelsToPoints(im,pixels):
    for p in pixels:
        im.putpixel(p[1],p[0])
    im.show()
    #return outimg
def grayScale(im,pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0]+px[0][1]+px[0][2])/3)
        draw.point(px[1],(gray_av,gray_av,gray_av))
def main():
    IMG_NAME = "piee"
    with Image.open(IMG_NAME+'.jpg') as im:
     pixels = storePixels(im)
     sorted_pixels = pixels.copy()
     n = len(sorted_pixels)
     l, w = im.size
     if (l, w) >= (300, 300):
         print("quick sort, the Image is large..")
         quickSortIterative(sorted_pixels, 0, n - 1)

     else:
         print("Selection sort, the image is not large..")
         selectionSort(sorted_pixels, comparePixels)


     sorted_im = pixelsToImage(im, sorted_pixels)
     sorted_im.save('sorted' + IMG_NAME + '.jpg', 'JPEG')
     grayScale(im, pixels)


     while(True):

          command = input("Type a value for red threshold oe Q to quit:")
          if (command == 'Q'):
              ImageType=input("Do you to save the image as jpg OR png")
              if (ImageType == 'jpg'):
               im.save( IMG_NAME + '.jpg')
               break
              if(ImageType == 'png'):
               im.save(IMG_NAME == 'png')
               break

          threshold = int(command)

          subi = binarySearchSub([r[0][0] for r in sorted_pixels],0,len(sorted_pixels)-1,threshold)
          grayScale(im, pixels)
          pixelsToPoints(im,sorted_pixels[subi:])
          im.show()



if __name__ == "__main__":
     main()