import cv2
import numpy as np
def face_check(img):
  # 顔のサイズ最小を定義
  face_min_size = (50, 50)
  
  # numpy配列じゃないとopencv対応してないので変換
  image = np.array(img)

  #グレースケール変換
  image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  #カスケード分類器の特徴量を取得する
  cascade = cv2.CascadeClassifier("./models/haarcascade_frontalface_default.xml")

  #物体認識（顔認識）の実行
  #image – CV_8U 型の行列．ここに格納されている画像中から物体が検出されます
  #objects – 矩形を要素とするベクトル．それぞれの矩形は，検出した物体を含みます
  #scaleFactor – 各画像スケールにおける縮小量を表します
  #minNeighbors – 物体候補となる矩形は，最低でもこの数だけの近傍矩形を含む必要があります
  #flags – このパラメータは，新しいカスケードでは利用されません．古いカスケードに対しては，cvHaarDetectObjects 関数の場合と同じ意味を持ちます
  #minSize – 物体が取り得る最小サイズ．これよりも小さい物体は無視されます
  facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=2, minSize=face_min_size)

  if len(facerect) > 0:
    return True
  else:
    return False