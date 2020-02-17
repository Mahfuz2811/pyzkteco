# -*- coding: utf-8 -*-
import sys
sys.path.append("zk")

from zk import ZK, const

conn = None
zk = ZK('10.29.254.204', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
try:
    print ('Connecting to device ...')
    conn = zk.connect()
    print ('Disabling device ...')
    conn.disable_device()
    print ('Firmware Version: : {}'.format(conn.get_firmware_version()))
    # print '--- Get User ---'
    users = conn.get_users()
    for user in users:
        privilege = 'User'
        if user.privilege == const.USER_ADMIN:
            privilege = 'Admin'
        print ('- UID #{}'.format(user.uid))
        print ('  Name       : {}'.format(user.name))
        print ('  Privilege  : {}'.format(privilege))
        print ('  Password   : {}'.format(user.password))
        print ('  Group ID   : {}'.format(user.group_id))
        print ('  User  ID   : {}'.format(user.user_id))

    print("get attendances")
    attendances = conn.get_attendance()
    for attendance in attendances:
        print ('- UID #{}'.format(attendance.uid))
        print ('  User  ID   : {}'.format(attendance.user_id))
        print ('  Time   : {}'.format(attendance.timestamp))

    print ("Voice Test ...")
    conn.test_voice()
    print ('Enabling device ...')
    conn.enable_device()
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()
