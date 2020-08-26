# docker运行nextcloud服务

从docker-hub查出next-cloud本来就支持ARM架构系统，直接拉取最新镜像：

```shell
docker pull nextcloud
```

为该服务创建单独的mysql用户：

```sql
# mysql -h127.0.0.1 -u root -p
> insert into mysql.user(Host,User,Password) values("%","nextcloud",password("123456"));
> 删除数据库
> drop database nextcloud;
> create database nextcloud;
> grant all privileges on nextcloud.* to nextcloud@0.0.0.0 identified by '123456';
> flush privileges;
```

运行nextcloud服务：

```
docker run -d \
    -p 8088:80 \
    --restart always \
    -v /data/nextcloud:/var/www/html \
    -e 'NEXTCLOUD_ADMIN_USER=user1' \
    -e 'NEXTCLOUD_ADMIN_PASSWORD=123456' \
    --link mariadb:mysql \
    -e 'MYSQL_HOST=mysql' \
    -e 'MYSQL_USER=nextcloud' \
    -e 'MYSQL_PASSWORD=123456' \
    -e 'MYSQL_ROOT_PASSWORD=123456' \
    -e 'MYSQL_DATABASE=nextcloud' \
    --name nextcloud \
    nextcloud
```

停止并删除nextcloud服务：

```shell
docker stop nextcloud
docker rm nextcloud
```

查看容器log:

```
docker logs -f nextcloud
```
