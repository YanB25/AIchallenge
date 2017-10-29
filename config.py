DEBUG = True

def debug_print(s):
    if DEBUG:
        print(s)
# for readJson.py
TotalNumber = 53879
BigBatch = 10000


# for CNN.py
pic_width = 500
pic_height = 500
pic_pixels = pic_width * pic_height
Categories = 80
Channel = 3

conv1_width = 5
conv1_height = 5
num_of_actmap1 = 32

conv2_width = 5
conv2_height = 5
num_of_actmap2 = 64

pic_aft_pool_w = pic_width / 4
pic_aft_pool_h = pic_height / 4

num_of_feature1 = 1024
