# mysql接口

- docs: <https://clickhouse.com/docs/zh/interfaces/mysql>

ClickHouse支持MySQL wire通讯协议。可以通过在配置文件中设置 mysql_port 来启用它:

```text
<mysql_port>9004</mysql_port>
```

使用命令行工具 `mysql` 进行连接的示例:

```shell
mysql --protocol tcp -u default -P 9004 -p
```

如果连接成功，则输出:

```text
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 2
Server version: 23.10.5.20-ClickHouse

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```

mysql 查询：

```text
mysql> use default;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+---------------+
| name          |
+---------------+
| cell_towers   |
| uk_price_paid |
+---------------+
2 rows in set (0.00 sec)
Read 2 rows, 74.00 B in 0.000841 sec., 2378 rows/sec., 85.93 KiB/sec.
```

mysql查询：

```text
mysql> SELECT formatReadableSize(total_bytes)
    -> FROM system.tables
    -> WHERE name = 'uk_price_paid'
    -> ;
+---------------------------------+
| formatReadableSize(total_bytes) |
+---------------------------------+
| 242.09 MiB                      |
+---------------------------------+
1 row in set (0.00 sec)
Read 1 rows, 31.00 B in 0.000893 sec., 1119 rows/sec., 33.90 KiB/sec.

```

mysql 查询：

```text
mysql> SELECT toYear(date) AS year,
    ->    round(avg(price)) AS price,
    ->    bar(price, 0, 1000000, 80
    -> )
    -> FROM uk_price_paid
    -> GROUP BY year
    -> ORDER BY year;
+------+--------+-----------------------------------------------------------------------------------------------------+
| year | price  | bar(round(avg(price)), 0, 1000000, 80)                                                              |
+------+--------+-----------------------------------------------------------------------------------------------------+
| 1995 |  67940 | █████▍                                                                                              |
| 1996 |  71516 | █████▋                                                                                              |
| 1997 |  78545 | ██████▎                                                                                             |
| 1998 |  85444 | ██████▊                                                                                             |
| 1999 |  96045 | ███████▋                                                                                            |
| 2000 | 107495 | ████████▌                                                                                           |
| 2001 | 118895 | █████████▌                                                                                          |
| 2002 | 137959 | ███████████                                                                                         |
...
29 rows in set (0.02 sec)
Read 80692 rows, 2.00 MiB in 0.014727 sec., 5479187 rows/sec., 135.86 MiB/sec.
```