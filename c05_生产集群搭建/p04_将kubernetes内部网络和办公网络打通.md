#### 基础信息：
- 参考文档： <https://zhuanlan.zhihu.com/p/187548589>
- 这里我们选择方案三，也就是加路由的方式来实现。

#### 操作说明：
```bash
# 其中：
#   kubernetes master节点IP：10.123.2.3/24
#   kubernetes node02节点IP：10.123.2.4/24
#   kubernetes集群--service-cluster-ip-range=10.96.0.0/12

# MacOS查看路由表：
netstat -nr

# MacOS上添加的静态路由规则如下：
sudo route -n add -net 10.96.0.0 -netmask 255.240.0.0 10.123.2.3

# MacOS上删除静态路由规则命令：
sudo route -n delete -net 10.96.0.0 -netmask 255.240.0.0 10.123.2.3

# 问题记录：
#   配上路由规则后，本地能ping通master节点上的pod，但ping不了node节点上的pod。
# 解法1：
#   暂时想到的是master节点需要开启路由转发功能，配置如下：
# 解法2：
#  将路由规则具体到节点的calico ip规则下：
# master节点
sudo route -n add -net 10.108.0.0 -netmask 255.255.0.0 10.123.2.3
# node02节点
sudo route -n add -net 10.107.0.0 -netmask 255.255.0.0 10.123.2.4

sudo route -n delete -net 10.108.0.0 -netmask 255.255.0.0 10.123.2.3
sudo route -n delete -net 10.107.0.0 -netmask 255.255.0.0 10.123.2.4

```
```bash
nslookup atlantis.master.svc.cluster.local
# 在master节点上是可以通过内部请求svc服务的：
http http://atlantis.master.svc.cluster.local:8000/ping/health

# 参考文章: <https://blog.csdn.net/snowrain1108/article/details/51734553>
# 查看mac Wi-Fi网卡的dns设置
networksetup -getdnsservers Wi-Fi
# 清除Wi-Fi网卡的dns设置
networksetup -setdnsservers Wi-Fi empty
```
