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
import datetime
import argparse

__author__ = 'timger & yishenggudou@gmail.com'
__license__ = 'MIT'
__version__ = (0, 0, 0)


def parse_args():
    p = argparse.ArgumentParser(description='hivetool: hive command tool.')
    p.add_argument('-F', '--DATEFORMAT', type=str,
                   default="%Y%m%d%H%M",
                   help="use dateformat parse datetime obj,default:%%Y%%m%%d%%H%%M")
    p.add_argument('-d', '--datetime', type=str,
                   default=datetime.datetime.now().strftime('%Y%m%d%H%M'),
                   help="the datetime map to url,default is datetime.datetime.now()")
    p.add_argument('-f', '--pathformat', type=str,
                   required=True,
                   help="the file path in hadoop like:/qlog/logs/{%%Y}/{%%Y%%m}/{%%Y%%m%%d}/{%%Y%%m%%d%%H}/*")
    p.add_argument('-t', '--hivetable', type=str,
                   required=True,
                   help="shoule map to hive table name")
    p.add_argument('-p', '--parition', type=str,
                   required=True,
                   help="hive table parition:day='{%%Y%%m%%d}',hour='{%%Y%%m%%d%%h}'")
    p.add_argument('-H', '--host', type=str,
                   help="hive Server's Host default use conf"
                   )
    p.add_argument('-P', '--port', type=int,
                   help="hive Server's Port, default use conf")
    return p


def main():
    from hive.table import Table
    p = parse_args()
    args = p.parse_args()
    datetime.datetime.strptime(args.datetime, args.DATEFORMAT)
    print args.DATEFORMAT, args.datetime
    t = Table(args.hivetable, args.host, args.port)
    t.load_from_dir(args.pathformat,
                    args.datetime,
                    args.parition)

if __name__ == '__main__':
    main()
