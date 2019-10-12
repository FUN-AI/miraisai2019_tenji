from menu import Menu
import unittest

class MenuTest(unittest.TestCase):

  def test_patmatch_short(self):
    menu = Menu()
    value = 'おはよう'
    pat = ['おはよう', 'こんにちは']
    self.assertEqual((0, True), menu.pat_match(value, pat))
  
  def test_patmatch_long(self):
    menu = Menu()
    value = 'どういうこと'
    pat = ['おはよう', 'こんにちは', 'さようなら', 'どういうこと', 'さくら']
    self.assertEqual((3, True), menu.pat_match(value, pat))
  
  def test_patmatch_InSentence(self):
    menu = Menu()
    value = 'おはようございます'
    pat = ['おはよう', 'こんにちは']
    self.assertEqual((0, True), menu.pat_match(value, pat))

  def test_read_json(self):
    menu = Menu()
    value = [["2", "3", "4"], "", "初めまして。何について知りたいですか？"]
    self.assertEqual(value, menu.pat_graph[0])
  
  def test_run(self):
    menu = Menu()
    _, pat = menu.run("")
    say, pat = menu.run(pat[0])
    self.assertEqual(3, len(pat))


if __name__ == '__main__':
  unittest.main()