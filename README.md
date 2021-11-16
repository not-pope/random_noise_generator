# Snow generator

Simple hacky script that generates random noise images (or *snow* image).

## Usage

Given that there are no requirments other than `random` and `typing` (which are
part of python's standard libs), there is no need to create/activate 
virtualenv, you just need `python3` interpreter.

`python3 main.py -w(idth) 500 -h(eight) 500 -b(lock_size) 10 -o(utput) my_image`

defaults:
  - -w 100
  - -h 100
  - -b 1
  - -o out.ppm

Generated image uses `ppm` format for the sake of simplicity, even tho there are
a plethora of other simple and fast libs for manipulating images. Because the 
image format is so simple, resulting image is bigger in size than other standard
formats. Resulting image, therefore, should not be uses on the web! (If you want
to use generated image in web app, convert it to some format that is better 
suited for the web).

Todo:
  - Add option to specify format of the resulting image (probably just convert 
  at the end)
  - Add option to specify color mode of the resulting image (currently it 
  supports only grayscale like *true* snow)
  - Optimize generating algorithm (remove damn loops..)