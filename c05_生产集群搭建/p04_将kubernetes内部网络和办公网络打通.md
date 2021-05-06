#### 基础信息：
- 参考文档A： <https://zhuanlan.zhihu.com/p/187548589>
- 参考文档B： <https://www.qikqiak.com/post/office-env-k8s-network/>

实验环境：
- MacOS下两台虚拟机组成的kubernetes集群，名称为master和node02，master机器同时也是一个node。
- Kubernetes版本： v1.19.3
- Kubernetes设置的
- master节点IP地址：10.123.2.3
- node02节点IP地址：10.123.2.4
- 两节点通过calico网络插件来实现集群内部网络的互通。
- master节点pod地址段：10.108.82.192/26
- node02节点pod地址段：10.107.14.192/26


#### 打通到kubernetes集群的IP访问：
MacOS命令记录：
```bash
# MacOS查看路由表：
netstat -nr

# 参考文章: <https://blog.csdn.net/snowrain1108/article/details/51734553>
# 命令行下查看mac Wi-Fi网卡的dns设置
networksetup -getdnsservers Wi-Fi
# 命令行下清除Wi-Fi网卡的dns设置
networksetup -setdnsservers Wi-Fi empty
```

理论上添加从MacOS到node节点和master节点的路由，就能打通到kubernetes pod & service cidr的访问:
```bash
# kubernetes master节点IP：10.123.2.3/24
# kubernetes node02节点IP：10.123.2.4/24
# kubernetes集群--service-cluster-ip-range=10.96.0.0/12

### MacOS上添加的静态路由规则如下：
# 对master pod地址段的访问，直接转到master节点
sudo route -n add -net 10.108.82.192 -netmask 255.255.255.192 10.123.2.3
# 对service 和 node pod的访问，直接转发到node节点
sudo route -n add -net 10.96.0.0 -netmask 255.240.0.0 10.123.2.4
# MacOS上删除静态路由规则命令：
# sudo route -n delete -net 10.108.82.192 -netmask 255.255.255.192 10.123.2.3
# sudo route -n delete -net 10.96.0.0 -netmask 255.240.0.0 10.123.2.4

# Linux
sudo route add -net 10.108.82.0 netmask 255.255.255.0 gw 10.123.2.3
sudo route add -net 10.96.0.0 netmask 255.240.0.0 gw 10.123.2.4
```

>  问题记录1：如果将数据包都转发到master节点，发现访问service的ip，是不行的，但将数据包转发到node节点可以实现。
>
> 问题记录2: calico是通过ipip隧道的方式打通node之间pod的访问，所以需要将访问master节点上的pod数据包，直接转发到master节点，这里的master上pod的地址段是10.108.82.0/24，不然这些pod会访问不了。
现在通过宿主机能正常访问kubernetes的service和pod。可以用`nslookup`工具测试访问service，用`ping`命令测试访问pod。

```bash
# 在master节点上尝试查询dns(不成功)
nslookup atlantis.master.svc.cluster.local
# 在master节点上是可以通过内部请求svc服务的：
http http://atlantis.master.svc.cluster.local:8000/ping/health
```

#### 打通到kubernetes的dns访问：
通过在node02节点部署dnsmasq服务实现。
```bash
cat > /etc/dnsmasq.d/default.conf <<-EOF
server=/cluster.local/10.96.0.10
EOF

# master节点添加如下iptables配置:
# 来自办公网络访问pod、service snat
# iptables -t nat -A POSTROUTING -s 10.123.2.0/24 -d 10.96.0.0/12 -j MASQUERADE
# 删除
# iptables -t nat -D POSTROUTING -s 10.123.2.0/24 -d 10.96.0.0/12 -j MASQUERADE

systemctl start dnsmasp
systemctl status dnsmasp
systemctl stop dnsmasp

# 查看53端口已经开启
netstat -lnpt |grep 53
```
将该node节点`/etc/resove.conf`的nameserver改为宿主机所在网段的nameserver，并将宿主机的dns指向该node节点即可。
