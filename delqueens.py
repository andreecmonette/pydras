class delBoard:
  def __del__(self):
    global __builtins__
    if not hasattr(self, 'myPos'):
      if not __name__ == "__main__":
        __builtins__ = delBoard
      __builtins__.nqueens = len(__name__) 
      __builtins__.ans = 0
      __builtins__.collected = 0
      for j in xrange(__builtins__.nqueens):
        a = delBoard()
        a.boardState = ((set(),set(),set()))
        a.myPos = j
        a = 0
      print str(__builtins__.collected) + " board states traversed."
      print "The number of "+str(__builtins__.nqueens)+"-queens solutions is: " + str(__builtins__.ans)
      return
    __builtins__.collected += 1 
    if self.myPos in self.boardState[0] or self.myPos in self.boardState[1] or self.myPos in self.boardState[2]:
      return
    if len(self.boardState[0]) == __builtins__.nqueens - 1:
      __builtins__.ans += 1 
      return
    c = self.boardState[0].copy()
    c.add(self.myPos)
    l = set(map(lambda x: x-1, self.boardState[1])).copy()
    l.add(self.myPos-1)
    l.discard(-1)
    r = set(map(lambda x: x+1, self.boardState[2])).copy()
    r.add(self.myPos+1)
    r.discard(__builtins__.nqueens)
    for k in xrange(__builtins__.nqueens):
      b = delBoard()
      b.boardState = (c,l,r)
      b.myPos = k
q = delBoard()
if __name__ == "__main__":
  print "Interrupt me!"
  while True:
    pass
