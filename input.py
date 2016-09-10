import os
import re
import stat
import sys
#import collections

process=raw_input("Enter a Process name or PID:")
os.system('sudo python parse.py '+process)

f_out=open('a.out','r')
if(os.path.getsize('a.out') <=0):
    print "Please enter a valid Process name or PID"
    sys.exit()

f=open('b.out','w')
os.chmod('b.out',stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
for line in file('a.out'):
     match = re.search(r'[0-9]+\.[0-9]+:.+', line)
     f.write(match.group(0)+'\n')
f.close()

dict={}

for line in file('b.out'):
    l=line.split()
    t=l[0]
    o=l[5]
    d=l[6]

    dict[float(t[:len(t)-1])]=[int(o.split('=')[1]),int(d.split('=')[1])]

#di=sorted(dict.items(),key=lambda t:t[0])

if process.isdigit():
    pid=int(process)
    print "\nMigration of task %d\n" %pid
else:
    print "\nMigration of task %s\n" %process

for key in sorted(dict):
    print "At time %f task migrates from cpu %d to cpu %d" %(key,dict[key][0],dict[key][1])

