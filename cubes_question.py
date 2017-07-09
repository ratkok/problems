#!/usr/bin/env python

import time
import collections

stime = time.time()
print "start time is: %s" % (stime)
aa = []
n = 30
for a in range (n+1):
    for b in range (n+1):
        for c in range (n+1):
            for d in range (n+1):
                if a**3 + b**3 == c**3 + d**3:
                    aa.append(tuple([a, b, c, d]))
                    break

etime = time.time()
print "found entries: %d" % (len(aa))
print "end time is: %s" % (etime)
print "Done in %d sec!" % (etime - stime)

stime = time.time()
print "with pow() start time is: %s" % (stime)
aa = []
n = 30
for a in range (n+1):
    for b in range (n+1):
        for c in range (n+1):
            if c**3 <= a**3 + b**3 :
                d = int(pow((a**3 + b**3 - c**3), 0.334))
                if d > n: 
                    continue
                if a**3 + b**3 == c**3 + d**3:
                    aa.append(tuple([a, b, c, d]))

etime = time.time()
print "found entries: %d" % (len(aa))
# print "entries:{}".format(aa)
print "end time is: %s" % (etime)
print "Done in %d sec!" % (etime - stime)

import pdb; pdb.set_trace()  # breakpoint 8756d1f8 //

stime = time.time()
print "with map start time is: %s" % (stime)
aaa = []
cc = set()
bb = collections.defaultdict(list)
n = 1000
for c in range (n+1):
    for d in range (n+1):
        result = c**3 + d**3
        bb[result].append(tuple([c,d])) 

for a in range (n+1):
    for b in range (n+1):
        result = a**3 + b**3
        matching = bb.get(result)
        if matching:
            for entry in matching:
                aaa.append(tuple([a, b, list(entry)]))
                cc.add(tuple([a, b, entry[0], entry[1]]))

etime = time.time()
print "found entries: %d" % (len(aaa))
# print "entries:{}".format(aa)
print "found entries: %d" % (len(cc))
# print "entries:{}".format(cc)

#for ent in aa:
#    if ent not in cc:
#        print ent
print "end time is: %s" % (etime)
print "Done in %d sec!" % (etime - stime)

obj = None
assert_is_none(obj)

stime = time.time()
print "with map2 start time is: %s" % (stime)
aaa = []
cc = set()
bb = collections.defaultdict(list)
n = 1000
for c in range (n+1):
    for d in range (n+1):
        result = c**3 + d**3
        bb[result].append(tuple([c,d])) 

for key,value in bb.items():
    for pair1 in value:
        for pair2 in value:
            aaa.append([pair1,pair2])


etime = time.time()
print "found entries: %d" % (len(aaa))
# print "entries:{}".format(aa)
print "found entries: %d" % (len(cc))
# print "entries:{}".format(cc)


print "end time is: %s" % (etime)
print "Done in %d sec!" % (etime - stime)

import random
stime = time.time()
print "diff finding start time is: %s" % (stime)

# my_array = [1, 7, 5, 9, 2, 12 ,3]
my_array = [int(1000*random.random()) for i in xrange(100000)]
my_hash = {key:True for key in my_array }
k = 125
sol = set()
for x in my_array:
    if my_hash.get(x+k):
        sol.add(tuple(sorted([x, x+k])))
    elif my_hash.get(x-k):
        sol.add(tuple(sorted([x, x-k])))


etime = time.time()
#print " starting array is: {}".format(my_array)
print "entries:{}".format(sol)
print "found entries: %d in array of %d elements" % ((len(sol), len(my_array)))
print "end time is: %s" % (etime)
print "Done in %d sec!" % (etime - stime)

print "end time is: %s" % (etime)
print "Done in %d sec!" % (etime - stime)

stime = time.time()
print "diff finding start time is: %s" % (stime)

my_big_string = 'qwertyuasdetrywudwsddyertfttgtreyssfrgtsguwdsertyytuwertyghghhghguwertyghghghghgnghjfujuwertyqdsa'
my_short_string = 'qauwertysd'
window = len(my_short_string)
from itertools import permutations
result = collections.defaultdict(list)
perms = [''.join(p) for p in permutations(my_short_string)]
#import pdb; pdb.set_trace()
for i in range(len(my_big_string) - 3):
    s_to_find =  my_big_string[i:i+len(my_short_string)]
    print s_to_find
    if s_to_find in perms:
        result[i] = my_big_string[i:i+len(my_short_string)]
        print "Found {}".format(s_to_find)

etime = time.time()
#print " starting array is: {}".format(my_array)
print "entries:{}".format(result)
print "found entries: %d in array of %d elements" % ((len(result), len(my_big_string)))
print "end time is: %s" % (etime)
print "Done in %d sec!" % (etime - stime)


