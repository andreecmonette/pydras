## WARNING: can only be killed with SIGTERM (^\), not SIGINT (^C)
## Causes fatal memory leak of size 2^51 objects in CPython, please kill

class LearneanPydra:
  def __init__(self, neck):
    self.neck = neck
  def __del__(self):
    LeftHead = LearneanPydra(self.neck + "l")
    RightHead = LearneanPydra(self.neck + "r")
    print self.neck

LearneanPydra("")

