# pycharm使用设置

系统： MacOS

##### 1. 如何实现pycharm格式化代码时，变量赋值时等号对齐?
结论：没有找到python代码该设置配置项，但javascript是有的：
- python代码格式配置路径：`Preferences | Editor | Code Style | Python`
- javascript代码格式配置路径：`Preferences | Editor | Code Style | JavaScript -> Wrapping and Braces -> Variable declarations -> Align`，选择`When grouped`即可。

##### 2. pycharm 字体设置：
常用字体类型：`JetBrains Mono`, `courier New`, 15, 1.1

IDE字体配置：`Preferences | Appearance & Behavior | Appearance | Use custom font:`

CODE字体配置路径：`Preferences | Editor | Font`

terminal配置路径：`Preferences | Editor | Color Scheme | Console Font`

##### 3. pycharm常用插件：
- 主题：`Gradianto`
- vim支持：`IdeaVim`
- 文件显示美化：`Atom Meterial Icons`
- bash语言支持：`BashSupport`
- 其它：`GitToolBox`
- 翻译：`Translation`
- mongo插件：`Mongo Plugin`
- requirements: `Requirements`
- minimap: `Code Glance`
- `Rainbow Brackets`
- `.ignore`
- `Kubernetes`
- `Grep Console`

##### 4. python代理设置：
设置路径：`Preferences | Appearance & Behavior | System Settings | HTTP Proxy`

历史配置：`HTTP raspi.com:1081`

##### 5. 其它相关设置
设置一行代码长度： `Preferences | Editor | Code Style | Hard wrap at`

设置不提醒`Duplicated code fragment`:

pycharm不自动折叠import代码: `Preferences | Editor | General | Code Folding | Ford by default | Imports`

pycharm连续缩进改为4空格(解决函数参数前空8个空格的问题)：`Preferences | Editor | Code Style | Python | Tabs and Indents | Continuation indent` 改为4
