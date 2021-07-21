#/usr/bin/env python3
""" This app check for loal disk and run Z dd processes to create Z files
"""
import threading
import subprocess
import time
import sys
import psutil





X=1000  # Disk size
Z=10    # count of files
Y=1000  #  file size
DATA = "/dev/zero" # Input data


def dd_func (infile, outpath , filename):
    """ dd runner function
    """
    cmd = ["dd", "if="+infile, "of="+outpath+filename, "bs=1", "count="+str(Y), "status=none"]
    start_time = time.time()
    process = subprocess.run(cmd, check=True)
    if process.returncode != 0:
        print (" Error running dd !!!!")
        sys.exit(1)
    print(filename+" --- %s seconds ---" % (time.time() - start_time))

hdds = psutil.disk_partitions (all=False)

for disk in hdds:
    size = psutil.disk_usage (disk.mountpoint)

    if size.free > X*1024*1024:
        for i in range(1,Z + 1):
            my_thread = threading.Thread \
                (target=dd_func,args=(DATA, disk.mountpoint, "./zz_test_"+str(i)+".test"))
            my_thread.start ()
        while threading.active_count () > 1:
            pass
        sys.exit(0)
