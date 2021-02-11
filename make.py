import PIL.Image as Image
import os
import argparse
import shutil
parser = argparse.ArgumentParser(description='find jpg files')
parser.add_argument('data', metavar='DIR',
                    help='path to root')
args = parser.parse_args()
IMAGES_PATH = args.data
x = os.listdir(IMAGES_PATH)
if not os.path.exists('jiafang'):
    os.mkdir('jiafang')
for n in range(300): 
     path = os.listdir(IMAGES_PATH+'/'+x[n])
     print(path[0])
     shutil.copy(IMAGES_PATH+'/'+x[n]+'/'+path[0],'jiafang')

