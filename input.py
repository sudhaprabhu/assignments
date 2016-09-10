import os
import re
import sys,getopt,time


s_time='5'
process=''

#take argument to the program
try:
    myopts, args = getopt.getopt(sys.argv[1:],"p:t:")
except getopt.GetoptError as e:
    print (str(e))
    print "Usage: python %s -p Process_Name/PID -t sleeptime" % sys.argv[0]
    sys.exit()
 
for o, a in myopts:
    if o == '-p':
        process=a
    elif o == '-t':
        s_time=a
    
if process=='':
    print "Please provide Process Name/PID"
    print "Usage: python %s -p Process_Name/PID -t sleeptime" % sys.argv[0]
    sys.exit()

if not s_time.isdigit():
    print "Please enter valid time"
    print "Usage: python %s -p Process_Name/PID -t sleeptime" % sys.argv[0]
    sys.exit()

########################################################################################


f_out=open('/tmp/a.out','w')
#invoke parse.py 
os.system('sudo python parse.py '+process+' '+s_time)

f_out=open('/tmp/a.out','r')
if(os.path.getsize('/tmp/a.out') <=0):
    print "Please enter a valid Process name or PID"
    os.remove('/tmp/a.out')
    sys.exit()


###########################################################################################

#store data in dictionary
dict={}

for line in file('/tmp/a.out'):
    match = re.search(r'[0-9]+\.[0-9]+:.+', line)
    ln=match.group(0).strip()
    l=ln.split()
    t=l[0]
    o=l[5]
    d=l[6]

    dict[float(t[:len(t)-1])]=[int(o.split('=')[1]),int(d.split('=')[1])]

#delete /tmp/a.out
os.remove('/tmp/a.out')

###########################################################################################

if process.isdigit():
    pid=int(process)
    print "\nMigration of task %d\n" %pid
else:
    print "\nMigration of task %s for time %fsec\n" %(process,float(s_time))


t=sorted(dict.keys())

#calucalte time delay 
delta=map(lambda x,y:y-x,t[:len(t)-1],t[1:])
delta.insert(0,0)


for i,key in zip(delta,sorted(dict)):
    time.sleep(i)
    print "At time %f task migrates from cpu %d to cpu %d" %(key,dict[key][0],dict[key][1])



#############################################################################################


