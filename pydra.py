## WARNING: can only be killed with SIGTERM (^\), not SIGINT (^C)

class Pydra:
  def __init__(self, neck):
    self.neck = neck
  def __del__(self):
    Pydra(self.neck + "l")
    Pydra(self.neck + "r")
    print self.neck

Pydra("")

