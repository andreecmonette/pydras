class Countdown:
  def __init__(self, count):
    self.count = count
  def __del__(self):
    Countdown(self.count+1)
    print self.count
Countdown(5)
