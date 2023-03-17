### 部署rancher

doc: <https://www.rancher.com/quick-start>

> 该文档记录时，安装的rancher版本是`v2.6.3`

参照官方文档：

- 01.Prepare a Linux Host
- 02.Start the server

  ```$ sudo docker run --privileged -d --restart=unless-stopped -p 80:80 -p 443:443 rancher/rancher```

##### rancher附带的k3s能关闭么？

rancher服务是通过docker启动的，内部运行的进程如下：
```text
[root@mint ~]$ docker exec -it rancher /bin/bash
bb48207d9b8c:/var/lib/rancher # ls
k3s  k3s-cluster-reset.log  k3s.log  management-state
bb48207d9b8c:/var/lib/rancher # ps auxf
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      440191  0.1  0.0  16692  5856 pts/0    Ss   01:28   0:00 /bin/bash
root      440265 75.0  0.0  38012  3840 pts/0    R+   01:28   0:00  \_ ps auxf
root           1  0.0  0.0   4408    64 ?        Ss   Mar15   0:03 tini -- rancher --http-listen-port=80 --https-listen-port=443 --audit-log-path=/var/log/auditlog/rancher-api-audit.log --audit-level=0 --audit-log-maxage=10 --audit-log-
root         210  2.3  2.8 1232660 320576 ?      Sl   Mar15  50:58 rancher --http-listen-port=80 --https-listen-port=443 --audit-log-path=/var/log/auditlog/rancher-api-audit.log --audit-level=0 --audit-log-maxage=10 --audit-log-maxbacku
root         222  0.0  0.4 833016 54308 ?        Sl   Mar15   1:05  \_ k3s init
root         239 11.7 10.3 12502564 1160040 ?    Sl   Mar15 255:48  |   \_ k3s server
root         254  0.4  0.7 838940 81052 ?        Sl   Mar15  10:30  |       \_ containerd
root        1643  0.0  0.2 716088 25564 ?        SLl  Mar15   0:15  \_ telemetry client --url https://localhost:443/v3 --token-key telemetry:n24psjd6m4hb452rmblxgfrwtcqkxdkgj64mvxv8zw7zqwbfscp9ms
root         707  0.0  0.0 714388  5068 ?        Sl   Mar15   0:20 /var/lib/rancher/k3s/data/e61cd97f31a54dbcd9893f8325b7133cfdfd0229ff3bfae5a4f845780a93e84c/bin/containerd-shim-runc-v2 -namespace k8s.io -id f53332ca12f3a61b3e6557045d2f
root         765  0.0  0.0   1020     4 ?        Ss   Mar15   0:00  \_ /pause
rancher     1030  0.1  0.4 773568 49016 ?        Ssl  Mar15   3:36  \_ fleetcontroller
root         804  0.0  0.0 714644  5456 ?        Sl   Mar15   0:23 /var/lib/rancher/k3s/data/e61cd97f31a54dbcd9893f8325b7133cfdfd0229ff3bfae5a4f845780a93e84c/bin/containerd-shim-runc-v2 -namespace k8s.io -id 60275f65387bca6cf340c4d92ffa
root         887  0.0  0.0   1020     4 ?        Ss   Mar15   0:00  \_ /pause
rancher     1166  0.1  0.2 742196 22732 ?        Ssl  Mar15   3:45  \_ gitjob --tekton-image rancher/tekton-utils:v0.1.3
root         881  0.0  0.0 714900  5696 ?        Sl   Mar15   0:20 /var/lib/rancher/k3s/data/e61cd97f31a54dbcd9893f8325b7133cfdfd0229ff3bfae5a4f845780a93e84c/bin/containerd-shim-runc-v2 -namespace k8s.io -id d93262f016236f1848c83d4330cc
root         978  0.0  0.0   1020     4 ?        Ss   Mar15   0:00  \_ /pause
root        1173  0.4  0.4 839952 51028 ?        Ssl  Mar15   9:36  \_ fleetagent
root        1028  0.0  0.0 714644  4948 ?        Sl   Mar15   0:21 /var/lib/rancher/k3s/data/e61cd97f31a54dbcd9893f8325b7133cfdfd0229ff3bfae5a4f845780a93e84c/bin/containerd-shim-runc-v2 -namespace k8s.io -id 4d5009111f138dc13a2c73b0dabd
root        1095  0.0  0.0   1020     4 ?        Ss   Mar15   0:00  \_ /pause
root        1277  0.3  0.1 748812 17416 ?        Ssl  Mar15   6:45  \_ /coredns -conf /etc/coredns/Corefile
root        1199  0.0  0.0 714644  4608 ?        Sl   Mar15   0:22 /var/lib/rancher/k3s/data/e61cd97f31a54dbcd9893f8325b7133cfdfd0229ff3bfae5a4f845780a93e84c/bin/containerd-shim-runc-v2 -namespace k8s.io -id 5b4a819a8a99d08f8543ea051233
root        1229  0.0  0.0   1020     4 ?        Ss   Mar15   0:00  \_ /pause
root        1328  0.1  0.3 749524 37684 ?        Ssl  Mar15   2:54  \_ webhook
```

可以看见k3s server是在rancher这一container内部运行着。

查看rancher支持的command和option，看是否能通过命令来关掉：
```text
bb48207d9b8c:/var/lib/rancher # rancher --help
NAME:
   rancher - Complete container management platform

USAGE:
   rancher [global options] command [command options] [arguments...]

VERSION:
   v2.6.3 (3c1d5fac3)

COMMANDS:
   help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS:
   --kubeconfig value              Kube config for accessing k8s cluster [$KUBECONFIG]
   --debug                         Enable debug logs
   --trace                         Enable trace logs
   --http-listen-port value        HTTP listen port (default: 8080)
   --https-listen-port value       HTTPS listen port (default: 8443)
   --k8s-mode value                Mode to run or access k8s API server for management API (embedded, external, auto) (default: "auto")
   --log-format value              Log formatter used (json, text, simple) (default: "simple")
   --acme-domain value             Domain to register with LetsEncrypt [$ACME_DOMAIN]
   --no-cacerts                    Skip CA certs population in settings when set to true
   --audit-log-path value          Log path for Rancher Server API. Default path is /var/log/auditlog/rancher-api-audit.log (default: "/var/log/auditlog/rancher-api-audit.log") [$AUDIT_LOG_PATH]
   --audit-log-maxage value        Defined the maximum number of days to retain old audit log files (default: 10) [$AUDIT_LOG_MAXAGE]
   --audit-log-maxbackup value     Defines the maximum number of audit log files to retain (default: 10) [$AUDIT_LOG_MAXBACKUP]
   --audit-log-maxsize value       Defines the maximum size in megabytes of the audit log file before it gets rotated, default size is 100M (default: 100) [$AUDIT_LOG_MAXSIZE]
   --audit-level value             Audit log level: 0 - disable audit log, 1 - log event metadata, 2 - log event metadata and request body, 3 - log event metadata, request body and response body (default: 0) [$AUDIT_LEVEL]
   --profile-listen-address value  Address to listen on for profiling (default: "127.0.0.1:6060")
   --features value                Declare specific feature values on start up. Example: "kontainer-driver=true" - kontainer driver feature will be enabled despite false default value [$CATTLE_FEATURES]
   --help, -h                      show help
   --version, -v                   print the version
```
观察得到里面并没有支持关闭k3s的选项，查到这里，我们暂时不进行下一步。

### rancher 权限控制
