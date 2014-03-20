
class delBoard:
  def __init__(self):   
    #self.boardState = boardState
    #self.myPos = myPos
    pass 
  def __del__(self):
    if not hasattr(self, 'myPos'):
      __builtins__.ans = 0
      __builtins__.collected = 0
      for j in xrange(8):
        a = delBoard()
        a.boardState = ((set(),set(),set()))
        a.myPos = j
        a = 0
      print str(__builtins__.collected) + " board states traversed."
      print "The number of 8-queens solutions is: " + str(__builtins__.ans)
      return
    __builtins__.collected += 1 
    if self.myPos in self.boardState[0] or self.myPos in self.boardState[1] or self.myPos in self.boardState[2]:
      return
    if len(self.boardState[0]) == 7:
      __builtins__.ans += 1 
      return
    c = self.boardState[0].copy()
    c.add(self.myPos)
    l = set(map(lambda x: x-1, self.boardState[1])).copy()
    l.add(self.myPos-1)
    l.discard(-1)
    r = set(map(lambda x: x+1, self.boardState[2])).copy()
    r.add(self.myPos+1)
    r.discard(8)
    for k in xrange(8):
      b = delBoard()
      b.boardState = (c,l,r)
      b.myPos = k
q = delBoard()
print "Interrupt me!"
while True:
  pass
