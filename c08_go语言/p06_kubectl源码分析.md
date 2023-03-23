# kubectl源码分析

### kubectl get cmd

对 `-o --output` 这一flag的实现逻辑：

- 提前定义好`o.ToPrinter`这一函数，里面会调用`printFlags.ToPrinter()`，通过命令行参数传入的`output`信息生成对应的printer，实现通过参数控制来选择打印机。
- 最后执行`GetOptions`的`Run`方法时，会调用自身`ToPrinter`这一变量指向的函数。

对 `--sort-by` 这一flag的实现逻辑：

- 在定义好的`o.ToPrinter`这一函数里添加逻辑，将获取到的printer通过`装饰器模式`进行装饰，装饰的内容是根据设置的`sort-by`信息对获取到的数据进行排序。
