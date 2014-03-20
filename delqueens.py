q = [0]*9
class delBoard:

  def __init__(self,boardState,myPos):   
    global q
    self.boardState = boardState
    self.myPos = myPos
    if self.myPos in self.boardState[0] or self.myPos in self.boardState[1] or self.myPos in self.boardState[2]:
      return
    if len(self.boardState[0]) == 7:
      q[8] += 1
      return
    a = len(self.boardState[0])
    c = self.boardState[0].copy()
    c.add(self.myPos)
    l = set(map(lambda x: x-1, self.boardState[1])).copy()
    l.add(self.myPos-1)
    l.discard(-1)
    r = set(map(lambda x: x+1, self.boardState[2])).copy()
    r.add(self.myPos+1)
    r.discard(8)
    q[len(c)] +=1
    for k in xrange(8):
      delBoard((c,l,r),k)
for j in xrange(8):    
  delBoard((set(),set(),set()),j)

print q[8]
