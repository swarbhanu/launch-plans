import sys
import time
from boto.ec2.connection import EC2Connection

def main():
    conn = EC2Connection()
    instances = conn.get_all_instances()
    print "Total: %d" % len(instances)
    count = 0
    for reserv in instances:
        for inst in reserv.instances:
            if inst.state == u'running':
                count += 1
    print "Running: %d" % count

if __name__ == "__main__":
    main()

