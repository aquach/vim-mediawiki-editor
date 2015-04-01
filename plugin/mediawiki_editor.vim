let s:initialized_python = 0
let s:script_path = fnamemodify(resolve(expand('<sfile>:p')), ':h')

function! s:InitializeClient()
  if !has('python')
    echo 'Error: this plugin requires vim compiled with python support.'
    finish
  endif

  if !s:initialized_python
    let s:initialized_python = 1
    execute 'pyfile ' . s:script_path . '/mediawiki_editor.py'
  endif
endfunction

function! s:MWRead(article_name)
  call <SID>InitializeClient()
  python mw_read(vim.eval('a:article_name'))
endfunction

function! s:MWWrite(article_name)
  call <SID>InitializeClient()
  python mw_write(vim.eval('a:article_name'))
endfunction

function! s:MWDiff(article_name)
  call <SID>InitializeClient()
  python mw_diff(vim.eval('a:article_name'))
endfunction

function! s:MWBrowse(article_name)
  call <SID>InitializeClient()
  python mw_browse(vim.eval('a:article_name'))
endfunction

command! -nargs=1 MWRead call <SID>MWRead(<f-args>)
command! -nargs=? MWWrite call <SID>MWWrite()
command! -nargs=? MWDiff call <SID>MWDiff()
command! -nargs=? MWBrowse call <SID>MWBrowse()
