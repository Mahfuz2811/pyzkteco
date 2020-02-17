# -*- coding: utf-8 -*-
import sys

from zk import ZK, const

sys.path.append("zk")

conn = None
zk = ZK('10.29.254.204', port=4370, timeout=5)

try:
  conn = zk.connect()
  conn.disable_device()
  # zk.set_user(1, 'Mahfuz', 0, '', '1', '26')
  zk.set_user(2, 'Naim', 0, '', '1', '1002', '13565700')
  # zk.enroll_user('26')
  conn.enable_device()
except Exception as e:
    print ("Process terminate :".format(e))
finally:
    if conn:
        conn.disconnect()
