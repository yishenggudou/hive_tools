#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright 2011 timger
#    +Author timger
#    +Gtalk&Email yishenggudou@gmail.com
#    +Msn yishenggudou@msn.cn
#    +Weibo @timger http://t.sina.com/zhanghaibo
#    +twitter @yishenggudou http://twitter.com/yishenggudou
#    Licensed under the MIT License, Version 2.0 (the "License");

import sys
from conf import conf
sys.path.insert(0, conf['hive']['lib'])
from hive_service import ThriftHive
from hive_service.ttypes import HiveServerException
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


__author__ = 'timger & yishenggudou@gmail.com'
__license__ = 'MIT'
__version__ = (0, 0, 0)


"""
.. module:: useful_1
   :platform: Unix, Windows
   :synopsis: A useful module indeed.

.. moduleauthor:: Andrew Carter <andrew@invalid.com>


"""


class Hive(object):

    def __init__(self,
                 host=conf['hive']['host'],
                 port=conf['hive']['port']):
        self._client(host, port)

    def _client(self, host, port):
        print ">>> connect hive thrift server", host, ':', port
        self.transport = TSocket.TSocket(host, port)
        self.transport = TTransport.TBufferedTransport(self.transport)
        self.protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = ThriftHive.Client(self.protocol)
        self.transport.open()
        return self.client

    def get_client(self):
        try:
            return self._client()
        except Thrift.TException, tx:
            print "connect hive thrift server error:"
            print '%s' % (tx.message)
            return None

    def _exec(self, hsql):
        try:
            self.client.execute(hsql)
            return self.client.fetchAll()
        except HiveServerException, e:
            print "HiveServerException:", str(e)
            return None

    def __exit__(self):
        self.transport.close()
        print "close hive transport socket"

    def ptime(self, date_str, date_format='%Y%m%d%H%M'):
        u"""
        """
        import datetime
        date_str = (date_str + '0'*10)[:12]
        if hasattr(self, 'dateformat') and self.dateformat:
            date_format = self.dateformat
        k = datetime.datetime.strptime(date_str, date_format)
        print ">>> parse ptime", date_str, date_format, k
        return k
