# 配置harbor开机自启动
- 系统版本：`Linux elementaryos 5.3.0-62-generic #56~18.04.1-Ubuntu`
- 参考文档：<https://github.com/goharbor/harbor/issues/7008>

本想通过添加systemctl配置文件，实现开机自启动harbor，但尝试多次没有成功，最后通过supervisor实现harbor开机自启，内容如下：

文件路径：</etc/supervisor/conf.d/harbor.ini>

文件内容：
```
[program:harbor]
directory=/opt/harbor
command=/usr/local/bin/docker-compose -f /opt/harbor/docker-compose.yml up
stop-command=/usr/local/bin/docker-compose -f /opt/harbor/docker-compose.yml down
user=root
numprocs=1
process_name=task%(process_num)d
redirect_stderr=true
stdout_logfile_backups=0
stdout_logfile_maxbytes=0
stdout_logfile=/var/log/harbor.log
```
其中supervisor服务已设置为开机自启，且`supervisird.conf`读取的子配置文件改为`*.ini`。
