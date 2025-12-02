import cv2
import time


# カメラのキャプチャを開始する
cap = cv2.VideoCapture(0)

# フレームの幅と高さを設定する
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 出力するファイル名のプレフィックス
folder_path = r'C:\Users\sklov\Desktop\makingPRO\python\MotionTetlis\picture\rotate'
filename_prefix = r"\captured_image_"

# 撮影した写真の枚数
count = 1

# キー入力の変数を初期化する
key = -1

while key != 13:
    # 現在の時刻を取得する
    current_time = time.time()

    # カメラからフレームを読み込む
    ret, frame = cap.read()

    # フレームが正常に読み込まれた場合
    if ret:
        # ファイル名を設定する
        filename = folder_path + filename_prefix + str(count) + ".jpg"

        # 画像を保存する
        cv2.imwrite(filename, frame)

        # 撮影した写真の枚数を増やす
        count += 1

    # 次の撮影までの時間を計算する
    next_capture_time = current_time + 3
    sleep_time = max(0, next_capture_time - time.time())

    # 次の撮影まで待つ
    key = cv2.waitKey(int(sleep_time * 1000)) & 0xFF

# キャプチャを解放する
cap.release()