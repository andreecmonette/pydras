#Todo: import into ipython notebook

class Omnom:
  def __init__(self, myname):
    print "Created " + myname
    self.myname = myname
  def __del__(self):
    print self.myname + " omnomed!"
print "Set up Omnom"    
raw_input()
print "Returning Noname:"

Omnom("Noname")

raw_input()
print "Assigning A:"
a = Omnom("A")

raw_input()

print "Defererencing A with del:"
del a
print "Done dereferencing A:"

raw_input()

print "Assigning B:"
b = Omnom("B")

raw_input()

print "Reassigning B:"
b = "Something else"
print "Done reassigning B"

raw_input()

print "Making a nested structure:"
c = Omnom("c")
c.d = Omnom("c.d")
c.d.e = Omnom("c.d.e")

raw_input()

print "Dereferencing c:"
del c
print "Done dereferencing c"

raw_input()

print "Making a cycle:"
f = Omnom("f")
f.g = Omnom("f.g")

f.g.h = f
print "Set f.g.h to f"
print "Dereferencing f:"
del f

raw_input()

print "Explicitly trying to collect garbage:"
import gc
print str(gc.collect()) + " items found"
print "The uncollectable garbage is: " + str(gc.garbage)
print "gc.garbage[0] is " + gc.garbage[0].myname
print "gc.garbage[1] is " + gc.garbage[1].myname

raw_input()

print "Breaking cycle explicitly: "
print "gc.garbage[0].g = 0"
gc.garbage[0].g = 0
print "Collecting gc.garbage[:]:"
del gc.garbage[:]
gc.collect()

raw_input()
print "Garbage remaining: " + str(gc.garbage)


