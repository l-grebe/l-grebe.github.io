# harbor使用记录
- 官方文档：<https://goharbor.io/docs/2.1.0/>
- harbor版本：v1.10.6
- harbor安装路径：/opt/harbor/

### 生成Server证书

操作命令如下：
```bash
cd /opt/harbor/
mkdir ca_file && cd ca_file

DOMAIN='vmk8s.com'

openssl genrsa -out ca.key 4096

openssl req -x509 -new -nodes -sha512 -days 3650 \
 -subj "/C=CN/ST=Beijing/L=Beijing/O=example/OU=Personal/CN=${DOMAIN}" \
 -key ca.key \
 -out ca.crt

openssl genrsa -out ${DOMAIN}.key 4096

openssl req -sha512 -new \
    -subj "/C=CN/ST=Beijing/L=Beijing/O=example/OU=Personal/CN=yourdomain.com" \
    -key ${DOMAIN}.key \
    -out ${DOMAIN}.csr
```
