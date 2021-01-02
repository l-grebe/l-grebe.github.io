# elasticsearch 操作文档
- elasticsearch 版本： v7.10.1
- 参考文档: <https://www.ruanyifeng.com/blog/2017/08/elasticsearch.html>

### 基本操作
```bash
# 查看集群信息
http localhost:9200

# 查看当前节点的所有Index
http 'localhost:9200/_cat/indices?v'

# 新建和删除Index
http -f PUT 'localhost:9200/weather'
http 'localhost:9200/_cat/indices?v'
http -f DELETE 'localhost:9200/weather'

# 安装中文分词
将`https://github.com/medcl/elasticsearch-analysis-ik`对应版本的插件下载至本地，并解压到`elasticsearch-root/plugins/ik/`目录下即可(elasticsearch-root指代elasticsearch根目录)

# 写入样例数据
echo '
{
  "mappings": {
    "properties": {
      "user": {
        "type": "text",
        "analyzer": "ik_max_word",
        "search_analyzer": "ik_max_word"
      },
      "title": {
        "type": "text",
        "analyzer": "ik_max_word",
        "search_analyzer": "ik_max_word"
      },
      "desc": {
        "type": "text",
        "analyzer": "ik_max_word",
        "search_analyzer": "ik_max_word"
      }
    }
  }  
}' | http -f PUT 'localhost:9200/accounts' -j

# 查看所有Index
http 'localhost:9200/_cat/indices?v'
```

### 简单数据操作
```bash
# 新增记录
echo '
{
  "user": "张三",
  "title": "工程师",
  "desc": "数据库管理"
}' | http -f POST 'localhost:9200/accounts/_doc/1' -j

# 再增一条
echo '
{
  "user": "李四",
  "title": "高级工程师",
  "desc": "数据库管理, 服务管理"
}' | http -f POST 'localhost:9200/accounts/_doc/2' -j
# 查看记录
http 'localhost:9200/accounts/_doc/1?pretty=true'
# 查看不存在的记录
http 'localhost:9200/accounts/_doc/abc'
# 删除记录(先别删)
http DELETE 'localhost:9200/accounts/_doc/1'

# 更新记录
echo '
{
    "user" : "张三",
    "title" : "工程师",
    "desc" : "数据库管理，软件开发"
}' | http -f PUT 'localhost:9200/accounts/_doc/1' -j

# 查询所有记录
http 'localhost:9200/accounts/_doc/_search'

# 添加过滤条件的查询
echo '
{
  "query" : { "match" : { "desc" : "数据" }}
}' | http 'localhost:9200/accounts/_doc/_search'

# 指定返回数据条数，默认是10条
echo '
{
  "query" : { "match" : { "desc" : "数据" }},
  "size": 1
}' | http 'localhost:9200/accounts/_doc/_search'

# 通过from字段，指定位移
echo '
{
  "query" : { "match" : { "desc" : "数据" }},
  "from": 1,
  "size": 1
}' | http 'localhost:9200/accounts/_doc/_search'

# 逻辑运算
...
```
