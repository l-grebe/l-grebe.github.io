# 构建minio容器服务

文档日期：2020.04.17

由于GFW的原因，`Dockerfile.arm.release`文件变更为如下内容：

```dockerfile
FROM golang:1.13-alpine as builder

WORKDIR /home

ENV GOPATH /go
ENV CGO_ENABLED 0
ENV GO111MODULE on

ADD qemu-3.0.0+resin-arm.tar.gz .
RUN mv qemu-3.0.0+resin-arm/qemu-arm-static .
ADD minio.tar.gz .

FROM arm32v7/alpine:3.10

LABEL maintainer="MinIO Inc <dev@min.io>"

COPY dockerscripts/docker-entrypoint.sh /usr/bin/
COPY CREDITS /third_party/
COPY --from=builder /home/qemu-arm-static /usr/bin/qemu-arm-static

ENV MINIO_UPDATE off
ENV MINIO_ACCESS_KEY_FILE=access_key \
    MINIO_SECRET_KEY_FILE=secret_key \
    MINIO_KMS_MASTER_KEY_FILE=kms_master_key \
    MINIO_SSE_MASTER_KEY_FILE=sse_master_key

RUN \
     apk add --no-cache ca-certificates 'curl>7.61.0' 'su-exec>=0.2' && \
     echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf

COPY minio /usr/bin/minio

RUN \
     chmod +x /usr/bin/minio  && \
     chmod +x /usr/bin/docker-entrypoint.sh

EXPOSE 9000

ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]

VOLUME ["/data"]

CMD ["minio"]
```

其中`minio.tar.gz`, `qemu-3.0.0+resin-arm.tar.gz`,`minio`已提前通过代理下载好，下载命令如下：

```
cd ~
git clone https://github.com/minio/minio.git
tar -zcvf minio.tar.gz minio
cp minio.tar.gz minio/
cd minio/
wget https://github.com/balena-io/qemu/releases/download/v3.0.0%2Bresin/qemu-3.0.0+resin-arm.tar.gz
wget https://dl.min.io/server/minio/release/linux-arm/minio
```

构建images命令如下：

```
docker build -t husy/minio -f Dockerfile.arm.release .
```

运行容器命令：

```shell
docker run -d -p 9000:9000 --name minio \
  -e "MINIO_ACCESS_KEY=123456" \
  -e "MINIO_SECRET_KEY=111111" \
  --restart always \
  -v /data/minio:/data \
  -v /home/hu/.minio:/root/.minio \
  husy/minio server /data
```
