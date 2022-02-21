# Image Converter-Resizer Cli
A simple python image converter

## Installation

Install pillow using pip.

```bash
pip install pillow
```

## How to use:
### run
```bash 
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

To Converts jpg to png format
```bash
python resizer.py image.jpg -f png
```
To Converts png to jpg format
```bash
python resizer.py image2.png -f jpg 
```

2.Image resizing

To Resize jpg image
```bash
python resizer.py image.jpg -r 200x200
```
To Resize png image
```bash
python resizer.py image2.png -r 250x300
```

## Libraries used
-[pillow](https://python-pillow.org/)