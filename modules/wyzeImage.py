import cv2
import subprocess
import shlex  
import os.path
import cvlib as cv
from cvlib.object_detection import draw_bbox 
from PIL import Image

## directory path
ROOT_DIR = os.path.abspath(os.curdir)

## full size from live feed
liveImage = ROOT_DIR+ '\static\output.jpg'

class images:
  def __init__(self, car, left, top, right, bottom):
    self.car = car
    self.left = left
    self.top = top
    self.right = right
    self.bottom = bottom
    self.file = ROOT_DIR+ '/static/' + self.car + '.jpg'
    self._crop()
  
  ## crop image to specify position of each car
  def _crop(self): 
    global liveImage
    img = Image.open(liveImage)
    area = (self.left, self.top, self.right, self.bottom) #left, top, right, bottom
    cropped_img = img.crop(area)
    cropped_img.save(self.file)
  
  ## use opencv to detect if car object exists 
  def _check(self):
    image = cv2.imread(self.file)
    bbox, label, conf = cv.detect_common_objects(image)
    if not label:
        return False
    else:
        return True
        
        
## use of ffmpeg to save a screenshot of live video feed to jpg      
def saveLiveImage():
    rtsp="" #specify rtsp url
    command = 'ffmpeg -y  -i ' + rtsp+ ' -ss 00:00:01 -vframes 1 "' + liveImage  + '" -loglevel quiet' ## ffmpeg command
    subprocess.call(shlex.split(command))