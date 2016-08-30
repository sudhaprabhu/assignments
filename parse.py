import time
import os
import sys,stat
#import shutil

process=sys.argv[1]
s_time=sys.argv[2]

#empty the trace file
f_trace=open('/sys/kernel/debug/tracing/trace','w')
f_trace.write('')
f_trace.close()

#set content of filter file
f_filter=open('/sys/kernel/debug/tracing/events/sched/sched_migrate_task/filter','w')
if process.isdigit():
    pid=int(process)
    f_filter.write("pid==%d" %pid)
else:
    f_filter.write("comm==%s" %process)
f_filter.close()

#enable the event to be traced
f_enable=open('/sys/kernel/debug/tracing/events/sched/sched_migrate_task/enable','w')
f_enable.write('1')
f_enable.close()


time.sleep(float(s_time))

#disable the event from being traced
f_enable=open('/sys/kernel/debug/tracing/events/sched/sched_migrate_task/enable','w')
f_enable.write('0')
f_enable.write('0')
f_enable.close()

#copy trace file to /tmp/a.out
f_trace=open('/sys/kernel/debug/tracing/trace','r')
lines=f_trace.readlines()
f_out=open('/tmp/a.out','w')
os.chmod('/tmp/a.out',stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO)
f_out.writelines(lines[11:])

f_out.close()
f_trace.close()








