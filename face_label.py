import cv2
import numpy as np

# 画像データのディレクトリ
input_data_path = './face_save_image/org/img'

# 切り抜いた画像データ保存ディレクトリ
save_path = './face_save_image/cut/'

label_list = {
    'p1':0,
    'p2':1,
    'p3':2,
}

