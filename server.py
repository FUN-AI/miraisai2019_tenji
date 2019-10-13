from flask import Flask, render_template, jsonify, request
import base64
from PIL import Image
from io import BytesIO
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/<test>', methods=['GET'])
def testpage(test):
  return render_template('test.html', test=test)

@app.route('/video')
def testVideo():
  return render_template('videotest.html')

from face import face_check
@app.route('/image', methods=['POST'])
def getImage():
  # 取得したデータを画像に変換
  get_data = request.form['img']
  dec_data = base64.b64decode( get_data.split(',')[1] )
  # 画像がnullならerrorでるからキャッチで判別
  try:
    dec_img = Image.open(BytesIO(dec_data))
  except:
    return jsonify({'status': 0})
  
  # 顔認証
  if face_check(dec_img):
    print('face is looking...')
    return jsonify({'status': 1})
  else:
    #print('return 0')
    return jsonify({'status': 0})

@app.route('/voice')
def testVoice():
  return render_template('voice.html')

@app.route('/returnVoice', methods=['POST'])
def testMenu():
  return jsonify({'say': request.form['text'], 'menus': ['aa', 'bb']})

from menu import Menu
menu_controle = Menu()
@app.route('/menu', methods=['POST'])
def menu():
  print("the get text: " + request.form['text'])
  say_text, next_menus = menu_controle.run(request.form['text'])
  return jsonify({'say': say_text, 'menus': next_menus})

if __name__ == "__main__":
  app.run(debug=True, port=8080)