# kubernetes从私有仓库拉取镜像

- 参考文档： <https://kubernetes.io/zh/docs/tasks/configure-pod-container/pull-image-private-registry/>

### 在集群中创建保存授权令牌的 Secret

```
kubectl create secret docker-registry harbor-regcred \
  --docker-server=vmele.com \
  --docker-username=admin \
  --docker-password=you_password \
  --docker-email=you_email
```

检查Secret：
```
kubectl get secret harbor-regcred --output=yaml
```
