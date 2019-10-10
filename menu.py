import json, codecs
from os import chdir
from pykakasi import kakasi

class Menu:
  def __init__(self):
    self.switch = None
    self.returnmenu = []
    # 基本データ構造[[next, pat, say_value], [next, pat, say_value], ...]
    self.pat_graph = self.read_json()
    self.next_ptr = [0]
    self.did_ptr = 0
    kakasiKn2H = kakasi()
    kakasiKn2H.setMode('J', 'H')
    self.kn2hConv = kakasiKn2H.getConverter()
    kakasiKt2H = kakasi()
    kakasiKt2H.setMode('K', 'H')
    self.kt2hConv = kakasiKt2H.getConverter()

  def read_json(self):
    menu = []
    with codecs.open('menu.json', 'r', 'utf-8') as f:
      menu_json = json.load(f)
      menu_json = menu_json['data']
      for i in menu_json:
        menu.append([i['next'], i['pat'], i['say_value']])
    return menu
  
  def pat_match(self, v, pat=['おはよう', 'こんにちは']):
    # パターンに対してマッチングをする、マッチした配列番号を返しマッチングしなければ-1
    for i in range(len(pat)):
      if pat[i] in v:
        return i, True
    return self.did_ptr, False
  
  def get_next_pat(self):
    pat = []
    temp_ptr = []
    for i in self.next_ptr:
      pat.append(self.pat_graph[i][1])
      temp_ptr.append([int(i) for i in self.pat_graph[i][0]])
    return pat, temp_ptr
  
  def outmaker(self, num, temp_ptr):
    # outputを作成する
    # 発言のピックアップ
    self.did_ptr = self.next_ptr[num]
    say_value = self.pat_graph[self.did_ptr][2]
    # 次のパターンのポインタを取得
    self.next_ptr = temp_ptr[num]
    # 次のパターンの文字列配列を取得
    pat, _ = self.get_next_pat()
    return say_value, pat

  def run(self, v):
    v = self.kn2hConv.do(v)
    v = self.kt2hConv.do(v)
    
    if self.next_ptr==0:
      return self.outmaker(0, self.pat_graph[0][1])
    pat , temp_ptr = self.get_next_pat()
    num, match_result = self.pat_match(v, pat)
    
    if match_result:
      # マッチしたらoutputを作成
      return self.outmaker(num, temp_ptr)
    
    # マッチしなかったら過去のpatと発言を送る
    return self.pat_graph[num][2], pat
    
