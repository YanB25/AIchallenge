import config
from PIL import Image as pim
def getImageMatrixLabel(address, label, size = 1000, image_height = config.pic_height, image_width = config.pic_width):
    # return true_label 
    # config.debug_print('testing')
    # true_label = [[1 if k === label else 0 for k in range(config.Channel)] for j in label]

    # image = readImage(address)
    # image_matrix = np.array(image);
    mats, labels = photo_address(address, size)
    mats = [readImage(addr) for addr in mats]
    return mats, labels

def readImage(address):
    image = pim.open(address).resize([config.pic_width,config.image_height])
    return image

if __name__ == "__main__":
#code below        
    print( getImageMatrixLabel('../ai_challenger_scene_train_20170904')  )