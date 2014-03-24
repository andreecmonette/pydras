# uncomment to view tree structure
# import sys
# sys.setrecursionlimit(16)

## WARNING: can only be killed with SIGTERM (^\), not SIGINT (^C)
class Pydra:
  def __init__(self, neck):
    self.neck = neck
  def __del__(self):
    #print self.neck
    Pydra(self.neck + "l")
    Pydra(self.neck + "r")
Pydra("")

