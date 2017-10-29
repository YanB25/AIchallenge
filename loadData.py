import config
from readJson import *
from PIL import Image as pim
import numpy as np
def next_batch(address, size = 1000, image_height = config.pic_height, image_width = config.pic_width):
    mats, labels = photo_address(address, size)
    mats = [readImage("{}/scene_train_images_20170904/{}".format(address, filename)) for filename in mats]
    return mats, labels

def readImage(address):
    image = np.array(pim.open(address).resize([config.pic_width,config.pic_height]))
    return image

if __name__ == "__main__":
#code below        
    a,b = next_batch('../ai_challenger_scene_train_20170904')
    print(a[0].shape)
    print(b)
