###hive_tools

hive tools 一些hive批处理操作库

致力于简化hive操作和

基于thrift和hiveserver交互

```
python setup.py install
```

```
usage: hiveload.py [-h] [-F DATEFORMAT] [-d DATETIME] [-f PATHFORMAT] -t
                   HIVETABLE [-p PARITION] [-H HOST] [-r REDUCE] [-P PORT]
                   action

hivetool: hive command tool.

positional arguments:
  action                load|drop

optional arguments:
  -h, --help            show this help message and exit
  -F DATEFORMAT, --DATEFORMAT DATEFORMAT
                        use dateformat parse datetime obj,default:%Y%m%d%H%M
  -d DATETIME, --datetime DATETIME
                        the datetime map to url,default is
                        datetime.datetime.now() you can use [1d|2d|3d|nd...]
                        [1h|2h|3h|nh...]
  -f PATHFORMAT, --pathformat PATHFORMAT
                        the file path in hadoop
                        like:/qlog/logs/{%Y}/{%Y%m}/{%Y%m%d}/{%Y%m%d%H}/*
  -t HIVETABLE, --hivetable HIVETABLE
                        shoule map to hive table name
  -p PARITION, --parition PARITION
                        hive table parition:day='{%Y%m%d}',hour='{%Y%m%d%h}'
  -H HOST, --host HOST  hive Server's Host default use conf
  -r REDUCE, --reduce REDUCE
                        reduce datetime range:[day|am|pm]
  -P PORT, --port PORT  hive Server's Port, default use conf
```

###导入

导入文件到分区表
```
python scripts/hiveload.py -f /data/logs/{%Y%m%d} -t qlog -p "day='{%Y%m%d},hour='{%Y%m%d%H}'" -d 201304011200
```

```
>>>: load data inpath '/data/logs/20130401' into table qlog PARTITION ( day='20130401,hour='2013040112' )
```

###删除


###创建



###todo

+   hive表的drop操作 分区删除
+   hive表的创建
+   hive server 故障的监测和重启
