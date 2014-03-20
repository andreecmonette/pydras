class Omnom:
  def __init__(self, myname):
    print "Created " + myname
    self.myname = myname
  def __del__(self):
    print self.myname + " omnomed!"
    


Omnom("Noname")

a = Omnom("A")

print "Defererencing A:"
del a
print "Done dereferencing A:"

print "Assigning B:"
b = Omnom("B")


print "Reassigning B:"
b = "Something else"
print "Done reassigning B"


print "Making a nested structure:"
c = Omnom("c")
c.d = Omnom("c.d")
c.d.e = Omnom("c.d.e")
print "Dereferencing c:"
del c
print "Done dereferencing c"

print "Making a cycle:"
f = Omnom("f")
f.g = Omnom("f.g")

f.g.h = f
print "Set f.g.h to f"
print "Dereferencing f:"
del f

import gc


