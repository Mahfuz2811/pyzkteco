# -*- coding: utf-8 -*-
import sys
sys.path.append("zk")
from zk.user import User
from zk.finger import Finger

from zk import ZK, const

conn = None
zk = ZK('192.168.1.201', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
try:
    print ('Connecting to device ...')
    conn = zk.connect()
    print ('Disabling device ...')
    conn.disable_device()


    conn.get_user_template(6,5)

    print ("Voice Test ...")
    conn.test_voice()
    print ('Enabling device ...')
    conn.enable_device()
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()
