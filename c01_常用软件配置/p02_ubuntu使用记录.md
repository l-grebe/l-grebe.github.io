# ubuntu使用记录

* ubuntu系统默认壁纸系统路径：`/usr/share/backgrounds`
* ubuntu系统默认用户图标系统路径：`/usr/share/pixmaps/faces`
* ubuntu fcitx快捷键配置文件：`~/.config/fcitx/config`
* linux 查询系统日志工具journalctl查询某一服务日志样例：`journalctl -u trojan.service -f`

### ubuntu更换软件源
##### 基础信息

- 系统版本：ubuntu_server_16.04

##### 系统换源

将源换为中国的

```bash
cd /etc/apt
vim source.list
# 切换为命令模式并输入":%s/us.archive/cn.archive/g"即可
# 保存退出":wq"
apt-get update
```

切换为阿里源

```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak #备份
> /etc/apt/sources.list
sudo vim /etc/apt/sources.list #修改
sudo apt-get update #更新列表
```

阿里源内容如下：

```bash
deb http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ trusty-backports main restricted universe multiverse
```
