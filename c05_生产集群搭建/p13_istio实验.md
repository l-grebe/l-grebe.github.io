### 问题：

virtual service 和 destination rules 以及 kubernetes service 之间是什么关系？

### ans:

我们用istio官方的bookinfo例子作为基础样例来解释：https://istio.io/latest/zh/docs/examples/bookinfo/

先找到istio 对外部提供的NodePort：

```shell
# 参考文档: https://istio.io/latest/zh/docs/setup/getting-started/#download
# 命令如下: 
kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}'
```

则对productionpage 的外部访问地址如下：

```shell
echo "http://vmmint.com:24854/productpage"
```

部署好bookinfo示例，并设置好路由请求后，将reviews的service删掉，发现productpage页面的reviews无法响应请求，故目前virtual service 和 destination rules
是不能脱离service的。