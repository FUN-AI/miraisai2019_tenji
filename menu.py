class Menu:
  def __init__(self):
    self.switch = None
    self.returnmenu = []
    # 基本データ構造[[next, pat, say_value], [next, pat, say_value], ...]
    self.pat_graph = [[[1], '', 'hello'], [[], '', 'hoge']]
    self.next_ptr = [0]
    self.did_ptr = 0
  
  def pat_match(self, v, pat= ['おはよう', 'こんにちは']):
    # パターンに対してマッチングをする、マッチした配列番号を返しマッチングしなければ-1
    for i in range(len(pat)):
      if pat[i] in v:
        return i
    return -1
  
  def get_next_pat(self):
    pat = []
    temp_ptr = []
    for i in self.next_ptr:
      pat.append(self.pat_graph[i][1])
      temp_ptr.append(self.pat_graph[i][0])
    return pat, temp_ptr
  
  def outmaker(self, num, temp_ptr):
    # outputを作成する
    # 発言のピックアップ
    say_value = self.pat_graph[num][2]
    self.did_ptr = num
    # その発言が最後な場合
    if len(temp_ptr) == 0:
      self.next_ptr = 0
      return say_value, []
    # 次のパターンのポインタを取得
    self.next_ptr = temp_ptr[num]
    # 次のパターンの文字列配列を取得
    pat, _ = self.get_next_pat()
    return say_value, pat
  
  def run(self, v):
    if self.next_ptr==0:
      return self.outmaker(0, self.pat_graph[0][1])
    pat , temp_ptr = self.get_next_pat()
    num = self.pat_match(v, pat)
    if num == -1:
      return self.pat_graph[self.did_ptr][2], pat
    return self.outmaker(num, temp_ptr)
    
