#Breadth-first search
#import sys
#sys.setrecursionlimit(20)

class Stumps(list):
  def __del__(self):
    newHeads = Stumps()
    for head in self:
      print head
      newHeads.append(head + "l")
      newHeads.append(head + "r")
Stumps().append("")
