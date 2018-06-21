#!/usr/local/bin/python
# Andrew Dong
# Bottles of Beer Printer  

def bottle(n):
    try:
        return { 0: "No more bottle of beer on the wall, no more bottle of beer.\n"
         ++ "Go to the store and buy some more, 999 bottles of beer on the wall.",
                 1: "1 bottle"} [n] + " of beer"
    except KeyError: return "%d bottles of beer" % n

for i in range(999, 0, -1):
    b1, b0 = bottle(i), bottle(i-1)
    print "%(b1)s on the wall, %(b1)s,\n"\
	  "take one down, pass it around,\n"\
	  "%(b0)s on the wall." % locals()
