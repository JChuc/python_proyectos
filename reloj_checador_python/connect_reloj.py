#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  connect_reloj.py
#  
#  Copyright 2018 jorge <jorge.chuc@ahcacao.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from zk import ZK, const
import logging
from datetime import datetime

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',filename='registro.txt',level=logging.DEBUG)

logging.warning("cuidado")
logging.info("Ya te lo adverti")

conn = None
zk = ZK('192.168.0.121', port=4370, timeout=5)
try:
    print 'Connecting to device ...'
    conn = zk.connect()
    print 'Disabling device ...'
    conn.disable_device()
    print 'Firmware Version: : {}'.format(conn.get_firmware_version())
    # print '--- Get User ---'
    
    ###tamaño del usuarios
    users = conn.get_users()
    size_users = len(users)
    
    
    #########obtener  el sig. usuario uid, user_id
    
    
    print '- UID #{}'.format(users[size_users-1].uid)
    sig_usuario = users[size_users-1].uid + 1
    print 'Siguiente usuario uid ' + str(sig_usuario)
    sig_id_user = int(users[size_users-1].user_id) + 1
    print 'Siguiente usuario user_id ' + str(sig_id_user)
    
    
    
    ##########
    for user in users:
        privilege = 'User'
        if user.privilege == const.USER_ADMIN:
            privilege = 'Admin'

        print '- UID #{}'.format(user.uid)
        print '  Name       : {}'.format(user.name)
        print '  Privilege  : {}'.format(privilege)
        print '  Password   : {}'.format(user.password)
        print '  Group ID   : {}'.format(user.group_id)
        print '  User  ID   : {}'.format(user.user_id)
        print '  Card   : {}'.format(user.card)

    print "Voice Test ..."
    lista_s = conn.get_attendance()
    for l in lista_s:
        print 'user     :{}'.format(l.user_id)
        print 'time     :{}'.format(l.timestamp)
        print 'estatus  :{}'.format(l.status)
    #conn.clear_attendance()
    conn.test_voice()
    print 'Enabling device ...'
    conn.enable_device()
except Exception, e:
    print "Process terminate : {}".format(e)
finally:
    if conn:
        conn.disconnect()
