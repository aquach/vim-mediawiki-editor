let s:initialized_python = 0
let s:script_path = fnamemodify(resolve(expand('<sfile>:p')), ':h')

function! s:InitializeClient()
    if has('python')
        let s:pcommand = 'python'
        let s:pfile = 'pyfile'
    elseif has('python3')
        let s:pcommand = 'python3'
        let s:pfile = 'py3file'
    else
    echo 'Error: this plugin requires vim compiled with python support.'
    finish
  endif

  if !s:initialized_python
    let s:initialized_python = 1
        execute s:pfile . ' ' . s:script_path . '/mediawiki_editor.py'
  endif
endfunction

function! s:MWRead(article_name)
  call <SID>InitializeClient()
    execute s:pcommand . " mw_read(vim.eval('a:article_name'))"
endfunction

function! s:MWWrite(...)
  call <SID>InitializeClient()
    execute s:pcommand . " mw_write(vim.eval('a:000'))"
endfunction

function! s:MWDiff(...)
  call <SID>InitializeClient()
    execute s:pcommand . " mw_diff(vim.eval('a:000'))"
endfunction

function! s:MWBrowse(...)
  call <SID>InitializeClient()
    execute s:pcommand . " mw_browse(vim.eval('a:000'))"
endfunction

command! -nargs=1 MWRead call <SID>MWRead(<f-args>)
command! -nargs=? MWWrite call <SID>MWWrite(<f-args>)
command! -nargs=? MWDiff call <SID>MWDiff(<f-args>)
command! -nargs=? MWBrowse call <SID>MWBrowse(<f-args>)
