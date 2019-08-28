# webカメラ起動サンプルコード
# https://qiita.com/Gyutan/items/c670b498a65e21fc350e
from datetime import datetime
from time import sleep
import tkinter

import cv2
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title("QR reader")
root.geometry("640x480")
CANVAS_X = 640
CANVAS_Y = 480
# Canvas作成
canvas = tkinter.Canvas(root, width=CANVAS_X, height=CANVAS_Y)
canvas.pack()


# VideoCaptureの引数にカメラ番号を入れる。
# デフォルトでは0、ノートPCの内臓Webカメラは0、別にUSBカメラを接続した場合は1を入れる。
cap = cv2.VideoCapture(0)

cascade_file = "haarcascade_frontalface_default.xml"

def show_frame():
    global CANVAS_X, CANVAS_Y

    ret, frame = cap.read()
    if ret == False:
        print('カメラから画像を取得できませんでした')
    
    # グレースケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # カスケードファイルを利用して顔の位置を見つける
    cascade = cv2.CascadeClassifier(cascade_file)
    face_list = cascade.detectMultiScale(gray, minSize=(100, 100))
    
    for (x, y, w, h) in face_list:
        print("face_position:",x, y, w, h)
        color = (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, thickness = 5)
    
    #cv2.imshow('frame', frame)
    
    # BGRなのでRGBに変換
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # RGBからPILフォーマットへ変換
    image_pil = Image.fromarray(image_rgb)
    # ImageTkフォーマットへ変換
    image_tk = ImageTk.PhotoImage(image_pil)
    # image_tkがどこからも参照されないとすぐ破棄される。
    # そのために下のようにインスタンスを作っておくかグローバル変数にしておく
    canvas.image_tk = image_tk
    # global image_tk
    
    
    
    # ImageTk 画像配置　画像の中心が指定した座標x,yになる
    canvas.create_image(CANVAS_X / 2, CANVAS_Y / 2, image=image_tk)
    # Canvasに現在の日時を表示
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    canvas.create_text(CANVAS_X / 2, 30, text=now_time, font=("Helvetica", 18, "bold"))

    # 10msごとにこの関数を呼び出す
    canvas.after(10, show_frame)

show_frame()

root.mainloop()
