# harbor使用记录
- 官方文档：<https://goharbor.io/docs/2.1.0/>
- harbor版本：v1.10.6
- harbor安装路径：/opt/harbor/

### 生成Server证书

操作命令如下：
```bash
cd /opt/harbor/
mkdir ca_file && cd ca_file

DOMAIN='vmele.com'

# 1.Generate a private key.
openssl genrsa -out ca.key 4096

# 2.Generate a certificate signing request (CSR).
openssl req -x509 -new -nodes -sha512 -days 3650 \
 -subj "/C=CN/ST=Beijing/L=Beijing/O=example/OU=Personal/CN=${DOMAIN}" \
 -key ca.key \
 -out ca.crt

openssl genrsa -out ${DOMAIN}.key 4096

openssl req -sha512 -new \
    -subj "/C=CN/ST=Beijing/L=Beijing/O=example/OU=Personal/CN=${DOMAIN}" \
    -key ${DOMAIN}.key \
    -out ${DOMAIN}.csr

# 3.Generate an x509 v3 extension file.
cat > v3.ext <<-EOF
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
DNS.1=vmele.com
DNS.2=vmele
DNS.3=elementaryos
EOF

# 4.Use the v3.ext file to generate a certificate for your Harbor host.
openssl x509 -req -sha512 -days 3650 \
    -extfile v3.ext \
    -CA ca.crt -CAkey ca.key -CAcreateserial \
    -in ${DOMAIN}.csr \
    -out ${DOMAIN}.crt
```

### Provide the Certificates to Harbor and Docker
```bash
DOMAIN='vmk8s.com'

# 1.Copy the server certificate and key into the certficates folder on your Harbor host.
mkdir /data/harbor/cert
cp ${DOMAIN}.crt /data/harbor/cert/
cp ${DOMAIN}.key /data/harbor/cert/

# 2.Convert yourdomain.com.crt to yourdomain.com.cert, for use by Docker.
openssl x509 -inform PEM -in ${DOMAIN}.crt -out ${DOMAIN}.cert

# 3.Copy the server certificate, key and CA files into the Docker certificates folder on the Harbor host. You must create the appropriate folders first.
mkdir -p /etc/docker/certs.d/${DOMAIN}/
cp ${DOMAIN}.cert /etc/docker/certs.d/${DOMAIN}/
cp ${DOMAIN}.key /etc/docker/certs.d/${DOMAIN}/
cp ca.crt /etc/docker/certs.d/${DOMAIN}/

# 4.Restart Docker Engine.
systemctl restart docker
```
