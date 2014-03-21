## Just a fork bomb.

class EnthusiasticPydra:
  def __init__(self, neck):
    print neck
    EnthusiasticPydra(neck + "l")
    EnthusiasticPydra(neck + "r")
EnthusiasticPydra("")
