# IMAGE-PRO (Image Converter-Resizer Cli) 
A simple python image converter that helps to convert type and size of given image.

## Team members
1. Nidha Shoukhath KP[https://github.com/nidhashoukhath]
2. Athul sai[https://github.com/athulsai66]

## Team ID
Python / 429

## Link to video walkthrough
[https://www.loom.com/share/1514a81506124d97a25062e6d07d5829]


## How it works ?

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

## Installation

Install pillow using pip.

```bash
pip install pillow
```

## How to Run:
```bash 
python resizer.py [imagefilename] [operation] [argument]
```