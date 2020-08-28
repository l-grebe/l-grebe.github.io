# Linux日志文件总管—logrotate

##### logrotate简介：

日志文件包含了关于系统中发生的事件的有用信息，在排障过程中或者系统性能分析时经常被用到。对于忙碌的服务器，日志文件大小会增长极快，服务器会很快消耗磁盘空间，这成了个问题。除此之外，处理一个单个的庞大日志文件也常常是件十分棘手的事。

logrotate是个十分有用的工具，它可以自动对日志进行截断（或轮循）、压缩以及删除旧的日志文件。例如，你可以设置logrotate，让`/var/log/foo`日志文件每30天轮循，并删除超过6个月的日志。配置完后，logrotate的运作完全自动化，不必进行任何进一步的人为干预。另外，旧日志也可以通过电子邮件发送，不过该选项超出了本教程的讨论范围。

主流Linux发行版上都默认安装有logrotate包，如果出于某种原因，logrotate没有出现在里头，你可以使用apt-get或yum命令来安装。

##### 安装命令：

```shell
# 在Debian或Ubuntu上：
apt-get install logrotate cron

# 在Fedora，CentOS或RHEL上：
yum install logrotate crontabs
```

logrotate的配置文件是`/etc/logrotate.conf`，通常不需要对它进行修改。日志文件的轮循设置在独立的配置文件中，它（们）放在`/etc/logrotate.d/`目录下。

##### logrotate配置文件参数介绍：

假如现在存在一个/var/log/log-file的日志文件，我们配置logrotate来轮询该日志文件，创建的配置文件为/etc/logrotate.d/log-file，内容如下：

```shell
/var/log/log-file {
    monthly
    rotate 5
    compress
    delaycompress
    missingok
    notifempty
    create 644 root root
    postrotate
        /usr/bin/killall -HUP rsyslogd
    endscript
}

# monthly: 日志文件将按月轮循。其它可用值为‘daily’，‘weekly’或者‘yearly’。
# rotate 5: 一次将存储5个归档日志。对于第六个归档，时间最久的归档将被删除。
# compress: 在轮循任务完成后，已轮循的归档将使用gzip进行压缩。
# delaycompress: 总是与compress选项一起用，delaycompress选项指示logrotate不要将最近的归档压缩，压缩将在下一次轮循周期进行。这在你或任何软件仍然需要读取最新归档时很有用。
# missingok: 在日志轮循期间，任何错误将被忽略，例如“文件无法找到”之类的错误。
# notifempty: 如果日志文件为空，轮循不会进行。
# create 644 root root: 以指定的权限创建全新的日志文件，同时logrotate也会重命名原始日志文件。
# postrotate/endscript: 在所有其它指令完成后，postrotate和endscript里面指定的命令将被执行。在这种情况下，rsyslogd 进程将立即再次读取其配置并继续运行。
```

其中：`logrotate -f /etc/logrotate.d/log-file`可以强制执行该日志切割配置一次，达到测试的目的，可使用`man logrotate`命令查看相关手册资料。
