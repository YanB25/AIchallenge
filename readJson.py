from config import *
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
    if photo_address.data == None:
        with open(addr + '/scene_train_annotations_20170904.json') as data_file:
            photo_address.data = json.load(data_file)
            debug_print('first time read json, length {}'.format(str(len(photo_address.data))))
    if photo_address.cur_index > BigBatch - num_of_photo:
        random.shuffle(photo_address.data)
        debug_print('shuffle tranning data')
        photo_address.cur_index = 0
    index = photo_address.cur_index
    address = [photo_address.data[photo_address.ls[i]]["image_id"] for i in range(index, num_of_photo + index)]
    label = [photo_address.data[photo_address.ls[i]]["label_id"] for i in range(index, num_of_photo + index)]
    photo_address.cur_index += num_of_photo
    debug_print('get from {} to {}'.format(index, num_of_photo + index))
    return address, label
photo_address.ls = [i for i in range(TotalNumber)]
photo_address.data = None
photo_address.big_batch = BigBatch
photo_address.cur_index = 0

for i in range(200000):
    if (i % 100 == 0):
        print('time {}'.format(str(i)))
        photo_address("ai_challenger_scene_train_20170904")
