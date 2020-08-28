# linux bashrc配置

### 配置示例：
修改PS1变量：
```bash
# 亮色版本：
export PS1="\[\e[37;1m\][\[\e[36;1m\]\u\[\e[37m\]@\[\e[36m\]\h\[\e[33m\]\w\[\e[37m\]]\[\e[36m\]$\[\e[m\] "
# 暗色版本：
export PS1="\[\e[32m\][\[\e[35m\]\u\[\e[m\]@\[\e[36m\]\h\[\e[31m\]\W\[\e[32m\]]\[\e[36m\]$\[\e[m\] "
# IP版本：
# IP_ADDR=`ip a show enp0s31f6 |grep "inet " |awk '{print $2}' |awk -F'/' '{print $1}'`
IP_ADDR=`ip addr |grep 'inet ' |grep -v '127.0.0.1' |head -n1 |awk -F ' ' '{print $2}' |awk -F '/' '{print $1}'`
export PS1="\[\e[37;1m\][\[\e[36;1m\]\u\[\e[37m\]@\[\e[36m\]${IP_ADDR} \[\e[33m\]\w\[\e[37m\]]\[\e[36m\]$\[\e[m\] "
```
