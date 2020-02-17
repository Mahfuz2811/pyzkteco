# -*- coding: utf-8 -*-
import sys
sys.path.append("zk")

from zk import ZK, const

conn202 = None
conn204 = None
zk202 = ZK('10.29.254.202', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
zk204 = ZK('10.29.254.204', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
try:
    print ('Connecting to device 204...')
    conn204 = zk204.connect()
    print ('Disabling device 204...')
    conn204.disable_device()

    print ('Connecting to device 202...')
    conn202 = zk202.connect()
    print ('Disabling device 202...')
    conn202.disable_device()
    
    # finger = conn.get_user_template(uid=1, temp_id=6)
    # print('finger', finger)

    # users = conn204.get_users()
    # for user in users:
    #     print ('User #{}'.format(user))

    #     finger = conn204.get_user_template(uid=user.uid, temp_id=6)

    #     conn202.set_user(uid=user.uid, name=user.name, privilege=user.privilege, password=user.password, group_id=user.group_id, user_id=user.user_id, card=user.card)
    #     conn202.save_user_template(user, finger)

        # conn202.save_user_template(user, finger)


    # conn.save_user_template([uid:2, name:Naim user_id:1002], finger)
       

    print ("Voice Test 204...")
    conn204.test_voice()
    print ('Enabling device 204...')
    conn204.enable_device()

    print ("Voice Test 202...")
    conn202.test_voice()
    print ('Enabling device 202...')
    conn202.enable_device()

except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn204:
        conn204.disconnect()
    if conn202:
        conn202.disconnect()
