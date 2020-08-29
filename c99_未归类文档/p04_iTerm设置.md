# iTerm设置

主题下载地址：<https://github.com/mbadolato/iTerm2-Color-Schemes>

目前喜欢的主题： `Dracula`

item常用字体：`Meslo LG L DZ for Powerline`


### iTerm常用快捷键：

```bash
文档来源：https://www.jianshu.com/p/da7728a8a4d7

#### iterm下窗口操作
新建窗口：shift + command + d（横向）command + d（竖向）
关闭窗口：shift + command + w
进入窗口 1,2,3：option + command + 编号

#### iterm下标签页操作
新建标签页: Command + T
关闭标签页: Command + W
前一个标签页: Command + 左方向键，Shift + Command + [
后一个标签页: Command + 右方向键，Shift + Command + ]
进入标签页1，2，3…: Command + 标签页编号
*Expose 标签页: Option + Command + E（将标签页打撒到全屏，并可以全局搜索所有的标签页）

#### iterm下面板操作
垂直分割: Command + D
水平分割: Shift + Command + D
前一个面板: Command + [
后一个面板: Command + ]
切换到上/下/左/右面板: Option + Command + 上下左右方向键
:
#### 粘贴历史
使用Command + Shift + h 可以呼出粘贴历史，支持模糊检索。还可以设置将粘贴历史保存在磁盘上（Preferences -> General）
```

### item2添加http代理

```bash
# 文档链接：https://colobu.com/2018/09/05/set-proxy-for-iterm/

# 终端下运行如下命令即可(这里使用的是树莓派上的privoxy代理)：

### ~/.zshrc 配置内容如下：
################### privoxy 配置 ###################
alias proxy_start='sudo /usr/local/sbin/privoxy /usr/local/etc/privoxy/config'
# 打开代理
function proxy_on() {
    export no_proxy="localhost,127.0.0.1,localaddress,.localdomain.com"
    export http_proxy="http://raspi.com:1081"
    export https_proxy=$http_proxy
    echo -e "已开启代理"
}
# 关闭代理
function proxy_off(){
    unset http_proxy
    unset https_proxy
    echo -e "已关闭代理"
}
```
