# kubernetes从私有仓库拉取镜像

- 参考文档： <https://kubernetes.io/zh/docs/tasks/configure-pod-container/pull-image-private-registry/>

### 在集群中创建保存授权令牌的 Secret

```
kubectl create secret docker-registry harbor-regcred \
  --docker-server=https://vmele.com/v2/ \
  --docker-username=admin \
  --docker-password=password \
  --docker-email=email_address
```
> 若密码中含有特殊符号，可使用单引号。

检查Secret：
```
kubectl get secret harbor-regcred --output=yaml
```

`.dockerconfigjson` 字段的值是 Docker 凭据的 base64 表示。

要了解 `dockerconfigjson` 字段中的内容，请将 Secret 数据转换为可读格式：
```
kubectl get secret harbor-regcred --output="jsonpath={.data.\.dockerconfigjson}" | base64 --decode
```
