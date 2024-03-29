# elementoryos的dns解析不生效

#### 基础信息:
- 问题记录：宿主机已配置dns，网络中其它主机（windows，linuxmint）都能正常通过域名访问kubernetes集群服务，但elementoryos不可以，通过`sudo tcpdump udp`命令，发现dns的包都转到`224.0.0.251.mdns`的地方了，最终发现是`avahi-daemon.service`服务的锅。

#### 问题记录:

nslookup是通的：
```
husy@elementaryos:~$ nslookup httpbin.default.svc.cluster.local
Server:		127.0.0.53
Address:	127.0.0.53#53

Non-authoritative answer:
Name:	httpbin.default.svc.cluster.local
Address: 10.107.81.94
```

访问服务，不通：
```
husy@elementaryos:~$ http httpbin.default.svc.cluster.local

http: error: ConnectionError: HTTPConnectionPool(host='httpbin.default.svc.cluster.local', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7f2918a51c18>: Failed to establish a new connection: [Errno -2] Name or service not known',)) while doing GET request to URL: http://httpbin.default.svc.cluster.local/
```

停掉该服务后可以访问：
```
sudo systemctl stop avahi-daemon.socket
sudo systemctl stop avahi-daemon.service
```

再次测试：
```
husy@elementaryos:~$ http httpbin.default.svc.cluster.local
HTTP/1.1 200 OK
Access-Control-Allow-Credentials: true
Access-Control-Allow-Origin: *
Connection: keep-alive
Content-Length: 9593
Content-Type: text/html; charset=utf-8
Date: Thu, 06 May 2021 10:22:01 GMT
Server: gunicorn/19.9.0

...
```
解析成功!

但linuxmint也存在该服务，是正常的。

寻找发现是avahi-daemon和`.local`域问题，文档链接：`https://qastack.cn/unix/352237/avahi-daemon-and-local-domain-issues`

文档链接：`https://web.archive.org/web/20160608083415/http://avahi.org/wiki/AvahiAndUnicastDotLocal`

最终修改`/etc/nsswitch.conf`得已解决：
```shell
# 将如下行：
hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4
# 改为：
hosts: files dns mdns4
```
