#!/usr/bin/env python
#
# Builds a high-res image of Elementary Automata
#
# http://mathworld.wolfram.com/ElementaryCellularAutomaton.html
#
# Written by Josh Myer <josh@joshisanerd.com>
#
# This is actually not such good code, but it's simple, so it should
# be quick to tweak.
#

import sys
import Image

class Automaton:
    def __init__(self, ruleno):
        self.ruleno = ruleno

        self.patterns = [0,0,0,0, 0,0,0,0]

        for i in range(8):
            if (self.ruleno & 1<<i) == 1<<i:
                self.patterns[i] = 1

    def iterate(self, ain):
        a = [0,0] + ain + [0,0]

        o = map(lambda x: 0, a)
        o = o[1:-1] # cut off ends

        for i in range(len(a)-2):
            j = (a[i] << 2) + (a[i+1] << 1) + a[i+2]
            o[i] = self.patterns[j]

        return o

#import pdb; pdb.set_trace()
i = int(sys.argv[1])
a = Automaton(i)

XMAX=1001
YMAX=500

im = Image.new("L", (XMAX,YMAX), 255)


q = [1]
for i in range(YMAX):
    x0 = (XMAX-len(q))/2
    for j in range(len(q)):
        im.putpixel( (x0+j,i), q[j])

    q = a.iterate(q)


    x0 = (XMAX-len(q))/2
    for j in range(len(q)):
        im.putpixel( (x0+j,i), (1-q[j])*255)


im.save("small_image_%s.gif" % sys.argv[1])
