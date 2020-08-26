# vncserver安装与配置

安装vncserver：

```shell
sudo apt install -y vnc4server

# 设置vnc密码命令：
vnc4passwd
```

~/.vnc/xstartup配置文件示例：

```shell
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

# 支持fcitx输入法
export XMODIFIERS=@im=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx

# 共享粘贴板
vncconfig -nowin -iconic &
startxfce4 &
```

systemd配置文件/lib/systemd/system/vncserver.service：

```shell
[Unit]
Description=vncserver
After=network.target

[Service]
User=hu
Group=hu

Type=forking
ExecStart=/usr/bin/vncserver -geometry 1400x900 -alwaysshared :1
ExecStop=/usr/bin/vncserver -kill :1
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

启动及检查服务：

```shell
sudo systemctl daemon-reload
sudo systemctl start vncserver
sudo systemctl status vncserver

# 开机自启
sudo systemctl enable vncserver
```

查看用户登录记录：

```shell
tail -f ~/.vnc/home-2\:1.log
```
