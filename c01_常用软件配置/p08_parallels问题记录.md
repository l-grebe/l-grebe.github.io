# parallels问题记录


### parallels挂载物理磁盘
背景：从本人linux服务器上卸载下来一块2T的物理磁盘，但mac本身不支持ext4文件系统，故将该磁盘挂载到mac下parallels软件的linux虚拟机下。

使用prl_disk_tool工具将磁盘映射为一个hdd文件：
```shell
# prl_disk_tool: parallels软件里带有的工具
# --hdd: 后带的参数是将要创建的hdd文件存储路径
# /dev/disk7: 将要挂载的磁盘设备(本人系统下是`/dev/disk7`)，可以在 mac | 磁盘工具 里查看
/Applications/Parallels\ Desktop.app/Contents/MacOS/prl_disk_tool create -p --hdd /Volumes/虚机/Parallels/ST2000DM008-2FR102.hdd --ext-disk-path /dev/disk7

```

将创建的磁盘设备添加作为虚拟机的新硬盘，再次开机运行`fdisk -l`命令，即可看到该挂载磁盘了。
