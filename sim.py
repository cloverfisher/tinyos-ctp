from TOSSIM import *
import sys

nrNodes = 10

t = Tossim([]);
r = t.radio();

f = open("topo.txt","r")
lines = f.readline()
for line in lines
 s = line.split()
 if(len(s) > 0)
  if s[0] == "gain":
  r.add(int(s[1]),int(s[2]),float(s[3]))
  
 


t.addChannel("Console",sys.stdout);
noise = open("meyer-heavy.txt", "r")
for line in noise:
  str1 = line.strip()
  if str1:
    val = int(str1)
    for i in range(1, nrNodes):
      t.getNode(i).addNoiseTraceReading(val)

for i in range(1, nrNodes):
  print "Creating noise model for ",i;
  t.getNode(i).createNoiseModel()

for i in range(1, nrNodes):
  time = randint(t.ticksPerSecond(),10*t.ticksPerSecond())
  t.getNode(i).bootAtTime(time);
  


for i in range (2000):
	t.runNextEvent();

print 'simulation completed'
