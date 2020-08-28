# mac下快捷键记录

### 常用命令与快捷键
```shell
#### 查看进程：
ps aux |grep ss-local

#### 查看端口占用情况：
sudo lsof -nP -iTCP -sTCP:LISTEN  # 不加sudo只能查看当前用户的端口使用情况。

#### mac下软件间的切换
ctrl + 左方向键：切换到下一个全屏软件
ctrl + 右方向键：切换到上一个全屏软件
ctrl + 上方向键：查看所有软件缩略图

```


### mac_chrome快捷键

| 快捷键                     | 说明                   |
| -------------------------- | ---------------------- |
| commad + l                 | 跳转到地址栏           |
| command + r                | 刷新当前网页           |
| ctrl + tab                 | 切换到下一个标签页     |
| command + t                | 打开新标签页           |
| command + n（n代值数字键） | 跳转到第n个标签页      |
| command + shift + j        | 打开下载页             |
| ctrl + command + f         | 最大化或缩小最大化窗口 |

### mac安装python3
设置软链接：
```shell
ln -s /usr/local/opt/python@3.7/bin/python3 /usr/local/bin/python3
ln -s /usr/local/opt/python@3.7/bin/pip3 /usr/local/bin/pip3

ln -s /usr/local/opt/python@3.7/bin/python3 /usr/local/opt/python/Frameworks/Python.framework/Versions/3.7/Python

```
