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
                   help="the file path in hadoop like:/qlog/logs/{%%Y}/{%%Y%%m}/{%%Y%%m%%d}/{%%Y%%m%%d%%H}/*")
    p.add_argument('-t', '--hivetable', type=str,
                   required=True,
                   help="shoule map to hive table name")
    p.add_argument('-p', '--parition', type=str,
                   help="hive table parition:day='{%%Y%%m%%d}',hour='{%%Y%%m%%d%%h}'")
    p.add_argument('-H', '--host', type=str,
                   help="hive Server's Host default use conf"
                   )
    p.add_argument('-r', '--reduce', type=str,
                   help="reduce datetime range:[day|am|pm]"
                   )
    p.add_argument('-P', '--port', type=int,
                   help="hive Server's Port, default use conf")
    p.add_argument('action', type=str,
                   default='load',
                   help="load|drop")
    return p


def main():
    from hive.table import Table
    p = parse_args()
    args = p.parse_args()
    datetime.datetime.strptime(args.datetime, args.DATEFORMAT)
    #print args.DATEFORMAT, args.datetime
    t = Table(args.hivetable, args.host, args.port)
    if args.action == 'load':
        if not args.pathformat:
            print "-f is required"
            raise
        if args.reduce == 'day':
            date_range = [args.datetime[:8]+('0000'+str(i))[-2:] for i in range(0,24)]
        elif args.reduce == 'am':
            date_range = [args.datetime[:8]+('0000'+str(i))[-2:] for i in range(0,13)]
        elif args.reduce == 'pm':
            date_range = [args.datetime[:8]+('0000'+str(i))[-2:] for i in range(13,24)]
        else:
            date_range = [args.datetime]
        for pt in date_range:
            t.load_from_dir(args.pathformat,
                            pt,
                            args.parition)
    elif args.action == "drop":
        print "drop"

if __name__ == '__main__':
    main()
