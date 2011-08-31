import sys
import time
from boto.ec2.connection import EC2Connection

def main():
    #print time.ctime()
    #time.sleep(4000)
    #print time.ctime()
    conn = EC2Connection()
    instances = conn.get_all_instances()

    for reserv in instances:
        for inst in reserv.instances:
            try:
	        if inst.state != u'terminated':
                    inst.terminate()
                    print "terminated %s" % inst
                    time.sleep(0.1)
                else:
                    print "already terminated: %s" % inst
            except SystemExit:
                raise
            except:
                print "* issue with %s" % inst


    y = """
    volumes = conn.get_all_volumes()
    #print volumes
    tenlist = []
    for volume in volumes:
        print "%s" % volume.attach_data.instance_id
        if volume.attach_data.instance_id:
            tenlist.append(volume.attach_data.instance_id)
        if len(tenlist) == 10:
            conn.terminate_instances(instance_ids=tenlist)
            time.sleep(2)
            tenlist = []
            print "\n-----\n"
    if tenlist:
        conn.terminate_instances(instance_ids=tenlist)
    """
    
    #print instances
    x = """
    for reserv in instances:
        for inst in reserv.instances:
            if inst.state == u'running':
                print "Terminating instance %s" % inst
            try:
                    inst.stop()
            except:
                print "issue with %s" % inst
    """

if __name__ == "__main__":
    main()

