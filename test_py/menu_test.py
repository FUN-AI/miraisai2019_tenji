import sys
sys.path.append('../')
from menu import Menu
import unittest

class MenuTest(unittest.TestCase):

  def test_patmatch_short(self):
    menu = Menu()
    value = 'おはよう'
    pat = ['おはよう', 'こんにちは']
    self.assertEqual(0, menu.pat_match(value, pat))
  
  def test_patmatch_long(self):
    menu = Menu()
    value = 'どういうこと'
    pat = ['おはよう', 'こんにちは', 'さようなら', 'どういうこと', 'さくら']
    self.assertEqual(3, menu.pat_match(value, pat))
  
  def test_patmatch_InSentence(self):
    menu = Menu()
    value = 'おはようございます'
    pat = ['おはよう', 'こんにちは']
    self.assertEqual(0, menu.pat_match(value, pat))
  
  def test_get_next_pat(self):
    menu =

if __name__ == '__main__':
  unittest.main()