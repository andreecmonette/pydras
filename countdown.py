class Countdown:
  def __del__(self):
    Countdown().count = self.count + 1
    print self.count
Countdown().count = 5
