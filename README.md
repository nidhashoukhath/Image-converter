# Image Converter-Resizer Cli
A simple python image converter

## Installation

Install pillow using pip.

```sh
pip install pillow
```

## How to use:
### run
```sh 
python resizer.py [imagefilename] [operation] [argument]
```

### imageFileName
Name of your image file
### operation 

-f  : To convert imgage format from jpg to png and viceversa

-r  : To resize the image

### argument

jpg : To convert to jpg format

png : To convert to png format

widthxheight : To resize eg. 200x200

### Examples:

1.Image format conversion

```sh
python resizer.py image.jpg -f png #Converts jpg to png format
```
```sh
python resizer.py image2.png -f jpg #Converts png to jpg format
```

2.Image resizing
```sh
python resizer.py image.jpg -r 200x200 #Resize jpg image
```
```sh
python resizer.py image2.png -r 250x300 #Resize png image
```

## Libraries used
-[pillow](https://python-pillow.org/)