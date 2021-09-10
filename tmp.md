### 临时记录

```bash
sudo yum install epel-release -y
sudo yum install htop -y
```


以下为临时数据

```shell
# 配置集群名称与服务地址
kubectl config --kubeconfig=${HOME}/.kube/config set-cluster cluster-name --server=https://{IP} --insecure-skip-tls-verify

# 设置一个管理用户为admin，并设置访问凭证。此处使用 用户名-密码 的验证方式
kubectl config --kubeconfig=${HOME}/.kube/config set-credentials admin --username=username --password=pwd

# 设置一个名为 admin 的配置，使用 cluster-name 集群与 admin 用户的上下文
kubectl config --kubeconfig=${HOME}/.kube/config set-context admin --cluster=cluster-name --namespace=test --user=admin

# 启用 admin 为默认上下文
kubectl config --kubeconfig=${HOME}/.kube/config use-context admin
```


```shell
# 配置集群名称与服务地址
./kubectl config --kubeconfig=${HOME}/.kube/config set-cluster cluster-name --server=https://10.123.2.3

# 设置一个管理用户为admin，并设置访问凭证。此处使用 用户名-密码 的验证方式
./kubectl config --kubeconfig=${HOME}/.kube/config set-credentials token=''

# 设置一个名为 admin 的配置，使用 cluster-name 集群与 admin 用户的上下文
./kubectl config --kubeconfig=${HOME}/.kube/config set-context admin --cluster=cluster-name --namespace=default

# 启用 admin 为默认上下文
./kubectl config --kubeconfig=${HOME}/.kube/config use-context admin
```
