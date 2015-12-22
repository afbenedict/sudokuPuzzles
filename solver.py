import scraper
import math
import time
import sys
from sys import stdin
import sys

SIZE = 9

def FindRow(i):
	return int(i/9)

def FindColumn(i):
	return i % 9

def CheckIfValidInRow(i):
	startNum = row * 9
	endNum = startNum + 9
	if(p[i] == 0):
		return true
	for j in range(startNum, endNum):
		if(i != j and p[j] != 0):
			if(p[i] == p[j]):
				return false

	return true



def CheckColumn():
	return false

def PrintGrid(p):
    i = 0
    for j in range(0, len(p)):
        if( j % 9 ==0) :
            print "\n",
            if( i == 3):
                for k in range(0, 11):
                    print "%-4s" % "-",
                print ""
                i = 1
            else:
                i += 1
        elif( j % 3 == 0 ):
            print "%-4s" % "|",
       
        print '%-4i' % p[j],
    print ""

def PrintMenu():
    print "Chose a level:"
    print "1. Easy"
    print "2. Medium"
    print "3. Hard"
    print "4. Impossible"



PrintMenu()
#get level back
#TODO simplify and add error checking
input = stdin.readline()
level = int(input)

p = scraper.GetPuzzle(level)
PrintGrid(p)



