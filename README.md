# movieShapeConverter  
movieShapeConverter is a script that can convert the movie shape to any rectangle size. 
  
It requires the following environments.  
* Python 3.5 or more
* OpenCV 3.4.3 or more (https://github.com/opencv/opencv)
* tqdm
 
You can use tqdm by bellow commands. 
```
$ pip install tqdm
```
 

# How to use
  
```
usage: movieShapeConverter.py [-h] [-c CONFIG] [-o OUTPUT] input resolution

positional arguments:
  input                 path to input movie
  resolution            resolution of converted movie

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        path to config file
  -o OUTPUT, --output OUTPUT
                        filename of output movie
```

'input':        file path of input movie. 
'resolution':   resolution of converted movie. width and length are connected by 'x'. ex) 2500x800 
'config':       path of config file. The Examination of config file is below. 
'output':       file name of converted movie. If you don't set this value, output file name is [input file name] + '_converted.np4' as default. 

During the script execution, you can stop the script when you press 'q'.   
Moreover, you can output the composite image of that moment into the same directory of this script when you press 'w'.  

# config file
You must make config file. 
4 coordinates used for projective transformation are described in this file. 

Each srcX coordinates are original coordinates of source movie. 
When you transform the coordinates of srcX, it becomes destX.


Example config file 
This example is converted from 4K movie to 2500x800 rectangle movie.
```
[number]
src1: 992 1096
src2: 2867 1100
src3: 417 1557
src4: 3387 1566

dest1: 0 0
dest2: 2500 0
dest3: 0 800
dest4: 2500 800
```

# example 
```
$ ./movieShapeConverter.py hoge.mp4 2500x800 movie.conf -o hogehoge.mp4 
```
# Contact
kome@hongo.wide.ad.jp
