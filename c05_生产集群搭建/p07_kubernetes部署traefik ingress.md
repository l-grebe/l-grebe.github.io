# kubernetes部署traefik ingress

#### 基础信息
- kubernetes version: v1.19.3
- 参考文档： <https://www.infoq.cn/article/2glspfgdiwg0uyz3v4tm>

#### 操作记录
将traefik作为kubernetes控制器，需要给该服务访问集群相关资源的权限：

traefik-cr.yaml:
```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: traefik-ingress
rules:
  - apiGroups:
      - ""
    resources:
      - services
      - endpoints
      - secrets
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - extensions
    resources:
      - ingresses
    verbs:
      - get
      - list
      - watch
```

traefik-crb.yaml
```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: traefik-ingress
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: traefik-ingress
subjects:
- kind: ServiceAccount
  name: traefik-ingress
  namespace: kube-system
```

traefik-service-acc.yaml
```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: traefik-ingress
  namespace: kube-system
```

traefik-deployment.yaml
```
kind: Deployment
apiVersion: apps/v1
metadata:
  name: traefik-ingress
  namespace: kube-system
  labels:
    k8s-app: traefik-ingress-lb
spec:
  replicas: 1
  selector:
    matchLabels:
      k8s-app: traefik-ingress-lb
  template:
    metadata:
      labels:
        k8s-app: traefik-ingress-lb
        name: traefik-ingress-lb
    spec:
      serviceAccountName: traefik-ingress
      terminationGracePeriodSeconds: 60
      containers:
      - image: traefik:v1.7
        name: traefik-ingress-lb
        ports:
        - name: http
          containerPort: 80
        - name: admin
          containerPort: 8080
        args:
        - --api
        - --kubernetes
        - --logLevel=INFO
```

traefik-svc.yaml
```yaml
kind: Service
apiVersion: v1
metadata:
  name: traefik-ingress-service
  namespace: kube-system
spec:
  selector:
    k8s-app: traefik-ingress-lb
  ports:
    - protocol: TCP
      port: 80
      name: web
    - protocol: TCP
      port: 8080
      name: admin
```

将以上yaml文件通过`kubectl create -f .`创建即可。

通过traefik web页面查看反向代理转发配置：
```
http://traefik-ingress-service.kube-system.svc.cluster.local:8080
```

添加ingress: ingress.yaml
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: minimal-ingress
  annotations:
    traefik.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - http:
      paths:
      - path: /httpbin
        pathType: Prefix
        backend:
          service:
            name: httpbin
            port:
              number: 80
      - path: /swagger
        pathType: Prefix
        backend:
          service:
            name: swagger
            port:
              number: 8080
```
通过`kubectl create -f ingress.yaml`命令创建ingress。

浏览器访问traefik并指定路径：
```
http://traefik-ingress-service.kube-system.svc.cluster.local/httpbin

http://traefik-ingress-service.kube-system.svc.cluster.local/swagger
```
这里拿`httpbin`和`swagger`两个服务做测试，流量确实转入对应的服务里了。
