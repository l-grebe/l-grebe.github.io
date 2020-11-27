# vimrc配置文件示例

```shell
set nocompatible                     " 关闭兼容模式
filetype off                         " 关闭文件类型检测

""""""""""""""""""""""""" vundle插件设置 """""""""""""""""""""""""
" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'The-NERD-tree'
Plugin 'tell-k/vim-autopep8'
Plugin 'Auto-Pairs'
Plugin 'L9'
Plugin 'tagbar'
" Plugin 'Valloric/YouCompleteMe'
Plugin 'tpope/vim-commentary'   " 注释插件
Plugin 'tpope/vim-rails'        " 自动配置'path'选项
" Plugin 'fatih/vim-go'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
" Plugin 'SirVer/ultisnips'
Plugin 'davidhalter/jedi-vim'
Plugin 'wchargin/vim-latexsuite'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'klen/python-mode'
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
Plugin 'mzlogin/vim-markdown-toc'
" Plugin 'Valloric/YouCompleteMe'
call vundle#end()               " required
filetype plugin indent on       " required
" To ignore plugin indent changes, instead use:
"filetype plugin on

""""""""""""""""""""""""" 基础设置 """""""""""""""""""""""""
set nu                          " 显示行号
syntax enable                   " 开启语法高亮功能
syntax on                       " 允许用指定语法高亮配色方案替换默认方案
set cul                         " 高亮光标所在行
set ruler                       " 显示光标当前位置
set scrolloff=3                 " 光标距离buffer顶部或底部3行
set noswapfile                  " 不要生成swap文件
set nobackup                    " no *~ backup files
set autoindent                  " 自动缩进
"let mapleader=';'               " 定义leader为';'
"set nocompatible               " not compatible with the old-fashion vi mode
set bs=2                        " allow backspacing over everything in insert mode
set history=1000                " 记录指定数量的命令行历史记录
set autoread                    " auto read when file is changed from outside
set wildmenu                    " 命令行模式智能补全
" set wildmode=longest:full
set wildmode=full
filetype indent on              " Enable filetype-specific indenting
filetype plugin on              " Enable filetype-specific plugins
let g:tex_flavor = "latex"
" auto reload vimrc when editing it
autocmd! bufwritepost .vimrc source %
" ignore these files while expanding wild chars
set wildignore=*.o,*.class,*.pyc
set smartindent
set copyindent                	" copy the previous indentation on autoindenting
set ignorecase                  " ignore case when searching 查找模式时不区分大小写
set smartcase                   " ignore case if search pattern is all lowercase,case-sensitive otherwise
set shortmess=atI
set showcmd                     " 显示输入的命令
if version >= 603
    set helplang=cn
    set encoding=utf-8
endif
set cmdheight=1                 " 命令行行高
set viminfo+=!                  " 保存全局变量
set iskeyword+=_,$,@,%,#,-      " 带有如下符号的单词不要被换行分割

""""""""""""""""""""""""" 分割窗口 """""""""""""""""""""""""
set splitbelow                  " 新分割窗口在下边
set splitright                  " 新分割窗口在右边
nnoremap <c-j> <c-w>j
nnoremap <c-h> <c-w>h
nnoremap <c-k> <c-w>k
nnoremap <c-l> <c-w>l

""""""""""""""""""""""""" 制表符设置 """""""""""""""""""""""""
set expandtab                   " 用空格代替制表符
" set softtabstop=4               " 让vim 把连续数量的空格视为一个制表符
" set tabstop=4                   " 制表符为4
set smarttab
au FileType Makefile set noexpandtab

" au BufNewFile,BufRead *.py
"     \ set tabstop=4
"     \ set softtabstop=4
"     \ set fileformat=unix
"
" au BufNewFile,BufRead *.js, *.html, *.css
"     \ set tabstop=2
"     \ set softtabstop=2
"     \ set shiftwidth=2

""""""""""""""""""""""""" path设置 """""""""""""""""""""""""
" set path+=`pwd`

""""""""""""""""""""""""" 搜索和匹配 """""""""""""""""""""""""
set ignorecase                  " 在搜索的时候忽略大小写
set hlsearch                    " 搜索结果高亮显示
set incsearch                   " incremental search

""""""""""""""""""""""""" 选择主题颜色 """""""""""""""""""""""""
if has("gui_running")            " GUI color and font settings
    set guifont=Osaka-Mono:h20
    set background=dark
    set t_Co=256                " 256 color mode
    set cursorline              " highlight current line
    colorscheme molokai
    gui=none cterm=none         " highlight CursorLine guibg=#003853 ctermbg=24
else
    " 终端颜色设置
    " colorscheme phd
    " colorscheme solarized
    " colorscheme molokai
    " colorscheme allomancer
    " colorscheme dracula
    colorscheme 1989
endif

""""""""""""""""""""""""" 编辑相关 """""""""""""""""""""""""
set backspace=indent,eol,start
set whichwrap=b,s,<,>,[,]
set mouse=                  	" 设置鼠标不管理窗口
set selectmode=
set mousemodel=popup
set keymodel=
set selection=inclusive
set noerrorbells               	" disable sound on errors
set novisualbell
" set t_vb=
" set tm=500

""""""""""""""""""""""""" 制表符设置 """""""""""""""""""""""""
set expandtab                   " replace <TAB> with spaces
set softtabstop=4               " 让 vim 把连续数量的空格视为一个制表符
set tabstop=4                   " 设置编辑时制表符占用空格数
set shiftwidth=4                " 设置格式化时制表符占用空格数
set smarttab
au FileType Makefile set noexpandtab

""""""""""""""""""""""""" 行显示时的设置 """""""""""""""""""""""""
"set nowrap                     " 禁止折行
set tw=120                      " 超过120字符折行
set lbr                         " 不在单词中间折行
set fo+=mB                      " 断行模块对亚洲语言的支持

""""""""""""""""""""""""" 底部状态栏设置 """""""""""""""""""""""""
set laststatus=2
" 状态行显示的内容
" set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%l,%v]\ [%p%%]\ %{strftime(\"%d/%m/%y\ -\ %H:%M\")}
" highlight StatusLine guifg=SlateBlue guibg=Yellow
" highlight StatusLineNC guifg=Gray guibg=White

function! CurDir()
    let curdir = substitute(getcwd(), $HOME, "~", "")
    return curdir
endfunction

function! HasPaste()
    if &paste
        return '[PASTE]'
    else
        return ''
    endif
endfunction

" C/C++ specific settings
autocmd FileType c,cpp,cc set cindent comments=sr:/*,mb:*,el:*/,:// cino=>s,e0,n0,f0,{0,}0,^0,:0,bs,g0,h1s,p2,t0,+2,(2,)20,*30

""""""""""""""""""""""""" ENCODING SETTINGS """""""""""""""""""""""""
set encoding=utf-8
set termencoding=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,utf-8,gb2312,big5,latin1

fun! ViewUTF8()
    set encoding=utf-8
    set termencoding=big5
endfun

fun! UTF8()
    set encoding=utf-8
    set termencoding=big5
    set fileencoding=utf-8
    set fileencodings=ucs-bom,big5,utf-8,latin1
endfun

fun! Big5()
    set encoding=big5
    set fileencoding=big5
endfun

""""""""""""""""""""""""" 去空行快捷键 """""""""""""""""""""""""
" nnoremap <F4> :g/^\s*$/d<CR>
" map <silent> <F4> :call Match_cword()<CR>
" func! Match_cword()
"     exe printf('match IncSearch /\V\<%s\>/', GetCurWord())
" endfun

""""""""""""""""""""""""" 去行尾空白符 """""""""""""""""""""""""
map <F7> :call DeleteTailSpace()<CR>
func! DeleteTailSpace()
    exec 'w'
    exec '%s/\v^(.{-})\s+$/\1/e'
    exec 'w'
    exec 'e! %'
endfun

""""""""""""""""""""""""" new generic makefile """""""""""""""""""""""""
au BufNewFile makefile,Makefile exec ":call Makefile()"
func! Makefile()
    " if filereadable("makefile") || filereadable("Makefile")
    "     echo "makefile exists"
    " else
        " vsp Makefile
    let content = ""
    let content .= "CC = gcc\nCXX = g++\n"
    let content .= "CFLAGS = -Wall -Wno-unused-result\n\n"
    let content .= "all: main\n\n"
    let content .= "%.o: %.c\n\t$(CC) -c -o $@ $< $(CFLAGS)\n"
    let content .= "%.o: %.cpp\n\t$(CXX) -c -o $@ $< $(CFLAGS)\n"
    call append(0, split(content, '\n'))
        " :w
    " endif
endfun

""""""""""""""""""""""""" 指定文件的扩展名 """""""""""""""""""""""""
if &filetype == 'python'
    set suffixesadd+=.py
endif

""""""""""""""""""""""""" 新文件标题 """""""""""""""""""""""""
"新建.c,.h,.py,.sh,.java文件，自动插入文件头
autocmd BufNewFile *.cpp,*.[ch],*.sh,*.py exec ":call SetTitle()"
""定义函数SetTitle，自动插入文件头
func! SetTitle()
    "如果文件类型为.sh文件
    if &filetype == 'sh'
        call setline(1,"\#!/bin/bash")
        call append(line("."), "")
    elseif &filetype == 'python'
        call setline(1,"#!/usr/bin/env python3")
        call append(line("."),"# encoding=utf-8")
        call append(line(".")+1, "")
        call append(line(".")+2, "")
    else
        call setline(1, "/******************************************************************")
        call append(line("."), "    > File Name: ".expand("%"))
        call append(line(".")+1, "    > Author: zhuyuan")
        call append(line(".")+2, "    > Mail: hu849434163@gmail.com")
        call append(line(".")+3, "    > Created Time: ".strftime("%c"))
        call append(line(".")+4, "****************************************************************/")
        call append(line(".")+5, "")
    endif
    if &filetype == 'c'
        call append(line(".")+6, "#include <stdio.h>")
        call append(line(".")+7, "#include <stdlib.h>")
        call append(line(".")+8, "")
        call append(line(".")+9, "int main(int argc, char *argv[])")
        call append(line(".")+10, "{")
        call append(line(".")+11, "")
        call append(line(".")+12, "    return 0;")
        call append(line(".")+13, "}")
    endif
    if expand("%:e") == 'h'
        call append(line(".")+6, "#ifndef _".toupper(expand("%:r"))."_H")
        call append(line(".")+7, "#define _".toupper(expand("%:r"))."_H")
        call append(line(".")+8, "#endif")
    endif
endfunc

"新建文件后，自动定位到文件末尾
autocmd BufNewFile * normal G

"C，C++ 按F5编译运行
map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
    exec "w"
    if &filetype == 'c'
        exec "!gcc % -o %< -std=gnu99 || make"
        exec "!time ./%<"
    elseif &filetype == 'cpp'
        exec "!g++ % -o %<"
        exec "!time ./%<"
    elseif &filetype == 'sh'
        :!time bash %
    elseif &filetype == 'python'
        exec "!time python2.7 %"
    elseif &filetype == 'html'
        exec "!firefox % &"
    elseif &filetype == 'go'
        exec "!time go run %"
    elseif &filetype == 'mkd'
        exec "!~/.vim/markdown.pl % > %.html &"
        exec "!firefox %.html &"
    elseif &filetype == 'javascript'
        exec "!time node %"
    endif
endfunc

""""""""""""""""""""""""" 实用设置 """""""""""""""""""""""""
" key shortcuts
" ;    mapleader=';'
" F2    YCM complete hint
" F3    YCM goto declaration
" F4
" F5    Compile and Run
" F6    Format
" F7    Delete Line-Tail space
" F8    Run GDB
" F9    Open or Close NerdTree Window
" F10
" F11
" F12   pastetoggle
" c-] upper a word

inoremap <c-]> <esc>viwUea
inoremap <c-c><c-c> <esc>:q<cr>
noremap <c-c><c-c> <esc>:q<cr>

nnoremap <leader>" viw<esc>a"<esc>hbi"<esc>lel
nnoremap <leader>' viw<esc>a'<esc>hbi'<esc>lel
nnoremap <leader>[ viw<esc>a]<esc>hbi[<esc>lel
nnoremap <leader>] viw<esc>a]<esc>hbi[<esc>lel
nnoremap <leader>{ viw<esc>a}<esc>hbi{<esc>lel
nnoremap <leader>} viw<esc>a}<esc>hbi{<esc>lel
nnoremap <leader>( viw<esc>a)<esc>hbi(<esc>lel
nnoremap <leader>) viw<esc>a)<esc>hbi(<esc>lel

" nmap <space> :
" vmap <space> :

" nmap <silent> <C-m> :nohlsearch<CR> " 该设置会导致quickfix功能中<CR>键失效

set clipboard+=unnamed  "共享剪贴板
set autowrite           "自动保存
set confirm             "处理未保存和只读文件时确认

set fillchars=vert:\ ,stl:\ ,stlnc:\    "分割窗口之间为空白
set showmatch           " 高亮显示匹配的括号
set matchtime=1         " 匹配括号高亮的时间（单位是十分之一秒）

""""""""""""""""""""""""" 代码折叠 """""""""""""""""""""""""
" set foldmethod=syntax   "按语法折叠代码 za zR zM"
" set nofoldenable
set foldmethod=indent
set foldlevel=99
" Enable folding with the spacebar
nnoremap <space> za

""""""""""""""""""""""""" 记忆退出时光标的位置 """""""""""""""""""""""""
if has("autocmd")
    au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
endif

function! ManFun(...)
    let cmd = "man "
    if a:0 == 1
        let cmd .= a:1
    elseif a:0 == 2
        let cmd .= a:1 . " " . a:2
    else
        echo "Arg err"
        return
    endif
    let manpage = system(cmd)
    pclose
    sp __Manpage
    normal! gg
    setlocal buftype=nofile bufhidden=delete noswapfile nowrap previewwindow
    call append(0, split(manpage, '\n'))
    setlocal nomodifiable
    setlocal nomodified
    setlocal filetype=man
    normal! gg
endfunction

function! GetCurWord()
    return expand("<cword>")
endfunction

command! -nargs=* Man call ManFun(<f-args>)
nnoremap K <esc>:call ManFun(GetCurWord())<cr>

""""""""""""""""""""""""" Plugin vim-indent-guides """""""""""""""""""""""""
" 随vim 自启动
let g:indent_guides_enable_on_vim_startup=1
" 从第二层开始可视化显示缩进
let g:indent_guides_start_level=2
" 色块宽度
let g:indent_guides_guide_size=1
" 快捷键 i 开/关缩进可视化
:nmap <silent> <Leader>i <Plug>IndentGuidesToggle"

""""""""""""""""""""""""" Plugin vim-airline """""""""""""""""""""""""
let g:airline_theme="luna"
"let g:airline_theme="solarized"
"let g:Powerline_colorscheme='solarized256'

"这个是安装字体后 必须设置此项"
let g:airline_powerline_fonts = 1

"打开tabline功能,方便查看Buffer和切换，这个功能比较不错"
"我还省去了minibufexpl插件，因为我习惯在1个Tab下用多个buffer"
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#buffer_nr_show = 1

" 设置切换Buffer快捷键"
" nnoremap <C-N> :bn<CR>
" nnoremap <C-P> :bp<CR>

" 关闭状态显示空白符号计数,这个对我用处不大"
let g:airline#extensions#whitespace#enabled = 0
let g:airline#extensions#whitespace#symbol = '!'

" 在Gvim中我设置了英文用Hermit， 中文使用 YaHei Mono "
if has('win32')
    set guifont=Hermit:h13
    set guifontwide=Microsoft_YaHei_Mono:h12
endif
"}

""""""""""""""""""""""""" Plugin ultisnips """""""""""""""""""""""""
"绝对路径
let g:UltiSnipsSnippetDirectories=[$HOME."/.vim/bundle/ultisnips/mysnippets/"]
let g:UltiSnipsExpandTrigger="<c-x>"
let g:UltiSnipsJumpForwardTrigger="<c-b>"
let g:UltiSnipsJumpBackwardTrigger="<c-z>"

""""""""""""""""""""""""" Plugin NERDTree """""""""""""""""""""""""
let NERDTreeWinSize=30
"列出当前目录文件
map <F9> :NERDTreeToggle<CR>
imap <F9> <ESC> :NERDTreeToggle<CR>
"当打开vim且没有文件时自动打开NERDTree
autocmd vimenter * if !argc() | NERDTree | endif
" 只剩 NERDTree时自动关闭
" autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTreeType") && b:NERDTreeType == "primary") | q | endif
" autocmd bufenter * if (winnr("$") == 1) | q | endif
set pastetoggle=<F12>
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree

""""""""""""""""""""""""" Plugin vim-go settings """""""""""""""""""""""""
let g:go_fmt_command = "goimports"
let g:go_template_autocreate = 0

""""""""""""""""""""""""" Plugin youdao-translate """""""""""""""""""""""""
vnoremap <silent> <C-y> :<C-u>Ydv<CR>
nnoremap <silent> <C-y> :<C-u>Ydc<CR>
noremap <leader>yd :<C-u>Yde<CR>

""""""""""""""""""""""""" Plugin python-mode """""""""""""""""""""""""
let g:pymode_rope = 0           " 代码补全，这里不使用
" Documentation
let g:pymode_doc = 1            " 通过命令:PymodeDoc arg查阅文档
let g:pymode_doc_key = 'K'      " 光标移到参数上面按快捷键K
" Linting
let g:pymode_lint = 1
" Default code checkers (you could set several)
let g:pymode_lint_checker = "pyflakes,pep8"
let g:pymode_lint_write = 1
let g:pymode_lint_cwindow = 0
let g:pymode_rope_autoimport = 1
let g:pymode_rope_autoimport_modules = ['os', 'shutil', 'datetime', 'time']
" Support virtualenv
let g:pymode_virtualenv = 1
"setup max line length
let g:pymode_options_max_line_length = 120
" Enable breakpoints plugin
let g:pymode_breakpoint = 1
let g:pymode_breakpoint_bind = '<leader>b'
" syntax highlighting
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
" Don't autofold code
" let g:pymode_folding = 0

""""""""""""""""""""""""" Plugin YCM """""""""""""""""""""""""
let g:ycm_global_ycm_extra_conf = '~/.vim/bundle/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py'
let g:ycm_key_invoke_completion = '<F2>'
let g:ycm_confirm_extra_conf = 0
let g:ycm_always_populate_location_list = 1
let g:ycm_enable_diagnostic_highlighting = 0
"map <F3> :YcmCompleter GoToDeclaration <CR>
map <F3> :YcmCompleter GoToDefinitionElseDeclaration<CR>
"let g:ycm_key_list_select_completion = ['','']
"let g:ycm_key_list_previous_completion = ['','']
set completeopt-=preview

""""""""""""""""""""""""" Plugin tagbar """""""""""""""""""""""""
"autocmd vimenter * Tagbar
noremap <F10> :Tagbar<CR>
inoremap <F10> <esc>:Tagbar<CR>a
let g:tagbar_width=35

""""""""""""""""""""""""" Plugin ctags """""""""""""""""""""""""
" 设置 ctags 对哪些代码元素生成标签
let g:tagbar_type_cpp = {
    \ 'kinds' : [
        \ 'd:macros:1',
        \ 'g:enums',
        \ 't:typedefs:0:0',
        \ 'e:enumerators:0:0',
        \ 'n:namespaces',
        \ 'c:classes',
        \ 's:structs',
        \ 'u:unions',
        \ 'f:functions',
        \ 'm:members:0:0',
        \ 'v:global:0:0',
        \ 'x:external:0:0',
        \ 'l:local:0:0'
     \ ],
     \ 'sro'        : '::',
     \ 'kind2scope' : {
         \ 'g' : 'enum',
         \ 'n' : 'namespace',
         \ 'c' : 'class',
         \ 's' : 'struct',
         \ 'u' : 'union'
     \ },
     \ 'scope2kind' : {
         \ 'enum'      : 'g',
         \ 'namespace' : 'n',
         \ 'class'     : 'c',
         \ 'struct'    : 's',
         \ 'union'     : 'u'
     \ }
\ }

""""""""""""""""""""""""" 代码格式化优化 """""""""""""""""""""""""
autocmd FileType python noremap <buffer> <F6> :call Autopep8()<CR>
" map <F6> :call FormartSrc()<CR><CR>
" "定义FormartSrc()
" func! FormartSrc()
"     exec "w"
"     if &filetype == 'c'
"         exec "!astyle --style=ansi -p -H --suffix=none %"
"     elseif &filetype == 'cpp' || &filetype == 'hpp'
"         exec "r !astyle --style=ansi --one-line=keep-statements -p -H -a --suffix=none %> /dev/null 2>&1"
"     elseif &filetype == 'py'||&filetype == 'python'
"         exec "r !autopep8 -i --aggressive %"
"     elseif &filetype == 'xml'
"         exec "!astyle --style=gnu --suffix=none %"
"     else
"         exec "normal gg=G"
"         return
"     endif
"     exec "e! %"
" endfunc
```
