from config import *
import time
import json
import random
from pprint import pprint
TotalNumber = 53879
# 
# with open('data.json') as data_file:    
#     data = json.load(data_file)
# 
# pprint(data)
# 
# print(data["maps"][0]["id"])

def photo_address(addr, num_of_photo = 1000):
    '''
    arg
        addr : the root address of training set. This function get info from "addr/*"
        num_of_photo : how many photos in a match
    returns
        address : mat in shape [num_of_photo, 1]
        label : mat in shape [num_of_photo, 1]
    '''
    if photo_address.data == None or photo_address.cur_index > BigBatch - num_of_photo:
        random.seed(time.time())
        random.shuffle(photo_address.ls)
        debug_print('shuffle tranning data')
        photo_address.cur_index = 0
    if photo_address.data == None:
        with open(addr + '/scene_train_annotations_20170904.json') as data_file:
            photo_address.data = json.load(data_file)
            debug_print('first time read json, length {}'.format(str(len(photo_address.data))))

    index = photo_address.cur_index
    address = [photo_address.data[photo_address.ls[i]]["image_id"] for i in range(index, num_of_photo + index)]
    label = [photo_address.data[photo_address.ls[i]]["label_id"] for i in range(index, num_of_photo + index)]
    photo_address.cur_index += num_of_photo
    debug_print('get from {} to {}'.format(index, num_of_photo + index))
    return address, label
photo_address.ls = [i for i in range(TotalNumber)]
photo_address.data = None
photo_address.cur_index = 0

if __name__ == "__main__":
    for i in range(200000):
        if (i % 100 == 0):
            print('time {}'.format(str(i)))
            photo_address("ai_challenger_scene_train_20170904")
