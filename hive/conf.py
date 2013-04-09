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
import yaml
import os

DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
NAME_FILE = os.path.relpath(__file__)
CONF_NAME = 'hiveconf.yaml'

CONF_DIRS = [DIR_PATH, '/etc/', '/user/local/etc/']


def get_conf():
    for P in CONF_DIRS:
        cp = os.path.join(P, CONF_NAME)
        if os.path.isfile(cp):
            conf = yaml.load(open(cp))
            return conf
        else:
            print "conf not find in:", cp

conf = get_conf()
