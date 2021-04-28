#### 基础信息
- 文档地址: <https://github.com/kylemanna/docker-openvpn>

#### 部署测试：
```bash
docker pull kylemanna/openvpn:2.4
OVPN_DATA="ovpn-data-example"
docker volume create --name $OVPN_DATA
docker run -v $OVPN_DATA:/etc/openvpn --rm kylemanna/openvpn:2.4 ovpn_genconfig -u udp://vmk8s.com
docker run -v $OVPN_DATA:/etc/openvpn --rm -it kylemanna/openvpn:2.4 ovpn_initpki

# start
docker run -v $OVPN_DATA:/etc/openvpn -d -p 1194:1194/udp --cap-add=NET_ADMIN kylemanna/openvpn:2.4
# 生成没有密码的客户端证书
docker run -v $OVPN_DATA:/etc/openvpn --rm -it kylemanna/openvpn:2.4 easyrsa build-client-full CLIENTNAME nopass
# 使用嵌入式证书检索客户端配置
docker run -v $OVPN_DATA:/etc/openvpn --rm kylemanna/openvpn:2.4 ovpn_getclient CLIENTNAME > CLIENTNAME.ovpn
```
