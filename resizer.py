import sys
from PIL import Image

try:
    orgImageFileName = sys.argv[1]

    operation = sys.argv[2]

    argument = sys.argv[3]

    if operation == '-f':

        r = orgImageFileName.split('.')

        imageFileName = r[0]
    
        im = Image.open(orgImageFileName)

        rgb_im = im.convert("RGB")

        rgb_im.save(f"{imageFileName}.{argument}")

    elif operation == '-r':
    
        im = Image.open(orgImageFileName)

        r = argument.split('x')

        r_tuple = (int(r[0]),int(r[1]))

        resized_im = im.resize(r_tuple)

        resized_im.save(f"output_{orgImageFileName}")   
    
except:
    print('\n------------\tHELP\t-------------')
    print('python resizer.py [imagefilename] [operation] [argument]\n')
    
    

    print('-f:Format converter')
    print('\tpython resizer.py image.jpg -f png')
    print('\tpython resizer.py image2.png -f jpg\n')

    print('-r:Resize')
    print('\tpython resizer.py image.jpg -r 200x200')
    print('\tpython resizer.py image2.png -r 250x300')