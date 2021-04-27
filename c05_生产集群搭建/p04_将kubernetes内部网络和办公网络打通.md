#### 基础信息：
- 参考文档A： <https://zhuanlan.zhihu.com/p/187548589>
- 参考文档B： <https://www.qikqiak.com/post/office-env-k8s-network/>
- 最终使用文档B，也就是明阳的博客文章来实现

#### 文档A操作说明：
```bash
# MacOS命令记录：

# MacOS查看路由表：
netstat -nr

# 参考文章: <https://blog.csdn.net/snowrain1108/article/details/51734553>
# 查看mac Wi-Fi网卡的dns设置
networksetup -getdnsservers Wi-Fi
# 清除Wi-Fi网卡的dns设置
networksetup -setdnsservers Wi-Fi empty
```

```bash
# 其中：
#   kubernetes master节点IP：10.123.2.3/24
#   kubernetes node02节点IP：10.123.2.4/24
#   kubernetes集群--service-cluster-ip-range=10.96.0.0/12

# MacOS上添加的静态路由规则如下：
sudo route -n add -net 10.96.0.0 -netmask 255.240.0.0 10.123.2.3
# MacOS上删除静态路由规则命令：
# sudo route -n delete -net 10.96.0.0 -netmask 255.240.0.0 10.123.2.3
```

>  问题记录：
    配上路由规则后，本地能ping通master节点上的pod，但ping不了node节点上的pod。
  解法1：
    暂时想到的是master节点需要开启路由转发功能，也就是"参考文档二"的方法。
  解法2：
   将路由规则具体到None的calico ip规则下：


```bash
# 在master节点上尝试查询dns(不成功)
nslookup atlantis.master.svc.cluster.local
# 在master节点上是可以通过内部请求svc服务的：
http http://atlantis.master.svc.cluster.local:8000/ping/health
```


#### 文档B操作说明
```bash
# 开启转发
# vim /etc/sysctl.d/k8s.conf
net.ipv4.ip_forward = 1
# sysctl -p


# master节点添加如下iptables配置:
# 来自办公网络访问pod、service snat
iptables -t nat -A POSTROUTING -s 10.123.2.0/24 -d 10.96.0.0/12 -j MASQUERADE
# 删除
iptables -t nat -D POSTROUTING -s 10.123.2.0/24 -d 10.96.0.0/12 -j MASQUERADE
# MacOS上添加路由规则：
sudo route -n add -net 10.96.0.0 -netmask 255.240.0.0 10.123.2.3

```
