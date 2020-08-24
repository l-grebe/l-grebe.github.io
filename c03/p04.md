# 树莓派supervisor运行httpbin

##### pip3安装httpbin gunicorn:

```shell
cd /code/
git clone https://github.com/postmanlabs/httpbin.git
pip3 install --no-cache-dir httpbin (下载源码安装，当前版本是0.9.2)
pip3 install gunicorn==20.0.4
```

##### supervisor httpbin.conf配置文件：

```
[program:httpbin]
command=/home/pi/.local/bin/gunicorn -b 0.0.0.0:8080 httpbin:app -k gevent
process_name=process-%(process_num)d
stopsignal=KILL
user=pi
numprocs=1
numprocs_start=10
redirect_stderr=true
stdout_logfile_backups=0
stdout_logfile_maxbytes=0
stdout_logfile=/data/log/httpbin.log
```
