# Docker使用记录

### docker 添加proxy配置

查看dockerd systemd 配置文件路径：

```bash
[hu@10.200.6.154 ~/website]$ systemctl status docker |head -n3
● docker.service - Docker Application Container Engine
   Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2019-03-13 19:06:36 CST; 4 days ago
```

在/lib/systemd/system/docker.service配置文件[service]添加如下配置：

```bash
Environment="HTTP_PROXY=http://127.0.0.1:1081/"
```

重启docker server:

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker.service
sudo systemctl status docker.service
```

验证docker配置是否被加载：

```bash
[hu@10.200.6.154 ~]$ sudo systemctl show --property Environment docker
Environment=HTTP_PROXY=http://127.0.0.1:1081/
```

现在docker pull 获取image时会走HTTP_PROXY！！！

### docker构建服务示例

##### 构建mariadb

```bash
# 拉取镜像
docker pull mariadb

# 运行容器
docker run -d \
    -p127.0.0.1:3306:3306 \
    -v /data/mysqldb:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=root \
    --name mariadb mariadb:latest
```

##### 构建mariadb:10.1.17

```bash
# 拉取镜像
docker pull mariadb:10.1.17

# 查看镜像构建历史
docker history --no-trunc --format "{{.CreatedBy}}" mariadb:10.1.17

# 运行```mariadb:10.1.17```容器
docker run -p3306:3306 -v /data/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root --name mariadb10.1 mariadb:10.1.17
```

##### 构建swagger

```bash
docker pull swaggerapi/swagger-editor:v3.5.5
docker run -d -p 8080:8080 --name swagger swaggerapi/swagger-editor:v3.5.5

```

##### 构建mongodb container:

```bash
#!/usr/bin/env bash

# docker 查询mongo的image
docker search mongo

# docker下载mongo的image
docker pull mongo:3.4

# docker运行mongo容器
docker run -d \
    -p 127.0.0.1:27017:27017 \
    -v /data/mongodb:/data/mongodb \
    --name mongodb mongo:3.4 \
    --storageEngine wiredTiger
```

##### 构建redis

```bash
# redis 相关
docker search redis
docker pull redis
docker run -p 127.0.0.1:6379:6379 --name redis redis
```

##### 构建kennethreitz/httpbin

```bash
# httpbin 服务：
docker run -p 127.0.0.1:80:80 --name httpbin kennethreitz/httpbin
```

##### 构建rabbitmq

```bash
docker pull rabbitmq:3.6
docker run -d -p 127.0.0.1:5672:5672 --name rabbitmq rabbitmq:3.6
```


### docker minio 部署

- minio网址：<https://min.io/>
- minio docker 入门指南：<https://docs.minio.io/docs/minio-docker-quickstart-guide>

操作命令01(latest)：

```bash
# minio 稳定版image下载：
docker pull minio/minio

# 运行minio容器
docker run -p 9000:9000 --name minio \
  -v /data/minio:/data \
  -v /home/hu/.minio:/root/.minio \
  minio/minio server /data

# 或者执行如下命令，自定义ACCESS_KEY和SECRET_KEY
docker run -p 9000:9000 --name minio \
  -e "MINIO_ACCESS_KEY=123456" \
  -e "MINIO_SECRET_KEY=111111" \
  -v /data/minio:/data \
  -v /home/hu/.minio:/root/.minio \
  minio/minio server /data
```

操作命令02(edge)：

```bash
# minio edge image下载：
docker pull minio/minio:edge

# 或者执行如下命令，自定义ACCESS_KEY和SECRET_KEY
docker run -p 9000:9000 --name minio \
  -e "MINIO_ACCESS_KEY=123456" \
  -e "MINIO_SECRET_KEY=111111" \
  -v /data/minio:/data \
  -v /home/hu/.minio:/root/.minio \
  minio/minio:edge server /data
```

使用curl下载该对象存储文件示例：

```bash
curl -o fox.png "http://10.200.6.154:9000/03.image/fox.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=SDFIOHGSDKLFJOWNLVKEIOFWJS%2F20190327%2F%2Fs3%2Faws4_request&X-Amz-Date=20190327T090412Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=89de3eb44cbec8f765e4e6e090ad877a400d1f9d63d3ccfb7be4ed88b402651f"
```
