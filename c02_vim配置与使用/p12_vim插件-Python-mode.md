# vim插件-Python-mode
python-mode是封装了pylint、rope、pydoc、pep8和mccabe的vim插件，使用它可以让你快速地完成python的vim开发环境。

github地址：https://github.com/python-mode/python-mode

文档地址：https://github.com/python-mode/python-mode/blob/develop/doc/pymode.txt

在vim中输入:h pymode也可以查看



##### python-mode快捷键：

```shell
" Keys:
" K             Show python docs
" <Ctrl-Space>  Rope autocomplete
" <Ctrl-c>g     Rope goto definition
" <Ctrl-c>d     Rope show documentation
" <Ctrl-c>f     Rope find occurrences
" <Leader>b     Set, unset breakpoint (g:pymode_breakpoint enabled)
" [[            Jump on previous class or function (normal, visual, operator modes)
" ]]            Jump on next class or function (normal, visual, operator modes)
" [M            Jump on previous class or method (normal, visual, operator modes)
" ]M            Jump on next class or method (normal, visual, operator modes)
```



##### python-mode在.vimrc中的配置：

```shell
"------ Plugin python-mode{
"setup max line length
let g:pymode_options_max_line_length = 120

let g:pymode_rope = 0

let g:pymode_doc = 1 " 通过命令:PymodeDoc arg查阅文档
let g:pymode_doc_key = 'K' "光标移到参数上面按快捷键K

let g:pymode_lint = 1
let g:pymode_lint_checker = "pyflakes,pep8"
let g:pymode_lint_write = 1
let g:pymode_lint_cwindow = 0

let g:pymode_rope_autoimport = 1
let g:pymode_rope_autoimport_modules = ['os', 'shutil', 'datetime', 'time']

let g:pymode_virtualenv = 1

let g:pymode_breakpoint = 1
let g:pymode_breakpoint_bind = '<leader>b'

let g:pymode_syntax = 1
let g:pymode_syntax_all = 1
let g:pymode_syntax_indent_errors = g:pymode_syntax_all
let g:pymode_syntax_space_errors = g:pymode_syntax_all

"pymode 提示
let g:pymode_lint_todo_symbol = 'WW'
let g:pymode_lint_comment_symbol = 'CC'
let g:pymode_lint_visual_symbol = 'RR'
let g:pymode_lint_error_symbol = 'EE'
let g:pymode_lint_info_symbol = 'II'
let g:pymode_lint_pyflakes_symbol = 'FF'

let g:pymode_folding = 0
"}
```

以上的参数稍微做些介绍，如下：

- 按K允许查看Python文档
- 每次保存代码时自动检查，但仅适用 PyLint or PyFlakes
- 支持virtualenv
- 用<leader>b 增加一个 pdb快捷键（插入simport pdb; pdb.set_trace() ### XXX BREAKPOINT到你的代码中）
- 增强语法高亮和输入

该插件涉及到的python库：`ropo`,`pylama`



##### pylint介绍：

Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合代码风格标准（Pylint 默认使用的代码风格是 PEP 8，具体信息，请参阅参考资料）和有潜在问题的代码。目前 Pylint 的最新版本是 pylint-0.18.1。

pyline的message_type：

```
(C) 惯例。违反了编码风格标准
(R) 重构。写得非常糟糕的代码。
(W) 警告。某些 Python 特定的问题。
(E) 错误。很可能是代码中的错误。
(F) 致命错误。阻止 Pylint 进一步运行的错误。
```
