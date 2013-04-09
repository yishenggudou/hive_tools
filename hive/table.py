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

from hive import Hive

__author__ = 'timger & yishenggudou@gmail.com'
__license__ = 'MIT'
__version__ = (0, 0, 0)


"""

"""


class Table(Hive):

    def __init__(self, table, host=None, port=None, dateformat=None):
        if host and port:
            super(Table, self).__init__(self, host=host, port=port)
        elif host:
            super(Table, self).__init__(self, host=host)
        elif port:
            super(Table, self).__init__(self, port=port)
        self.tablename = table

    def render_time_str(self, str_format, ptime):
        import re
        ptime = self.ptime(ptime)
        args = re.findall('(\{[\s\S]*?\})', str_format)
        for p in args:
            rp = ptime.strftime(p.strip('{').strip('}'))
            str_format = str_format.replace(p, rp)
        return str_format

    def load_from_dir(self, dir_format, ptime, partition={}):
        if type(partition) == dict:
            _ = ["{0}='{1}'".format(*i) for i in partition.items()]
            partition = " ".join(_)
        else:
            _ = self.render_time_str(partition, ptime)
            partition = _
        if bool(partition):
            partition_str = "( " + partition + " )"
        else:
            partition_str = ''
        if partition_str:
            hsql = "load data inpath '{hadoop_dir}' into table {table} PARTITION {partition}"
        else:
            hsql = "load data inpath '{hadoop_dir}' into table {table}"
        hadoop_dir = self.render_time_str(dir_format, ptime)
        hsql = hsql.format(hadoop_dir=hadoop_dir,
                           table=self.tablename,
                           partition=partition_str)
        print ">>>:", hsql
        return
        resutes = self._exec(hsql)
        for l in resutes:
            print l
        if resutes:
            return True
        else:
            return False
