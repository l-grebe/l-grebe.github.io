# vim插件-autopep8
要想在vim里能快速格式化python代码，需要安装autopep8库：

ubuntu 安装：```pip install autopep8```



##### 在.vimrc里绑定快捷键：

```shell
"代码格式化优化

map <F6> :call FormartSrc()<CR><CR>

"定义FormartSrc()
func! FormartSrc()
    exec "w"
    if &filetype == 'c'
        exec "!astyle --style=ansi -p -H --suffix=none %"
    elseif &filetype == 'cpp' || &filetype == 'hpp'
        exec "r !astyle --style=ansi --one-line=keep-statements -p -H -a --suffix=none %> /dev/null 2>&1"
    elseif &filetype == 'py'||&filetype == 'python'
        exec "r !autopep8 -i --aggressive %"
    elseif &filetype == 'xml'
        exec "!astyle --style=gnu --suffix=none %"
    else
        exec "normal gg=G"
        return
    endif
    exec "e! %"
endfunc
```

用vim打开python代码，按F6就可以格式化python代码了！！！
