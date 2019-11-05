if exists('g:loaded_mediawiki_editor')
    finish
endif
let g:loaded_mediawiki_editor = 1

let s:initialized_python = 0
let s:script_path = fnamemodify(resolve(expand('<sfile>:p')), ':h')

function! s:InitializeClient()
  if has('python')
    let s:python_command = 'python'
    let pyfile_command = 'pyfile'
  elseif has('python3')
    let s:python_command = 'python3'
    let pyfile_command = 'py3file'
  else
    echo 'Error: this plugin requires vim compiled with python support.'
    finish
  endif

  if !s:initialized_python
    let s:initialized_python = 1
    execute pyfile_command . ' ' . s:script_path . '/mediawiki_editor.py'
  endif
endfunction

function! s:MWRead(article_name)
  call <SID>InitializeClient()
  execute s:python_command . " mw_read(vim.eval('a:article_name'))"
endfunction

function! s:MWBacklinks(...) abort
  call <SID>InitializeClient()
  execute s:python_command . " mw_backlinks(vim.eval('a:000'))"
endfunction

function! s:MWMove(new_name) abort
  call <SID>InitializeClient()
  execute s:python_command . " mw_move(vim.eval('a:new_name'))"
endfunction

function! s:MWMoveNoRedirect(new_name) abort
  call <SID>InitializeClient()
  execute s:python_command . " mw_move_no_redirect(vim.eval('a:new_name'))"
endfunction

function! s:MWWrite(...)
  call <SID>InitializeClient()
  execute s:python_command . " mw_write(vim.eval('a:000'))"
endfunction

function! s:MWDiff(...)
  call <SID>InitializeClient()
  execute s:python_command . " mw_diff(vim.eval('a:000'))"
endfunction

function! s:MWSearch(...) abort
  call <SID>InitializeClient()
  execute s:python_command . " mw_search(vim.eval('a:000'))"
endfunction

function! s:MWSubpages(...) abort
  call <SID>InitializeClient()
  execute s:python_command . " mw_subpages(vim.eval('a:000'))"
endfunction

function! s:MWBrowse(...)
  call <SID>InitializeClient()
  execute s:python_command . " mw_browse(vim.eval('a:000'))"
endfunction


command! -nargs=1 MWRead call <SID>MWRead(<f-args>)
command! -nargs=? MWBacklinks call <SID>MWBacklinks(<f-args>)
command! -nargs=? MWMove call <SID>MWMove(<f-args>)
command! -nargs=? MWMoveNoRedirect call <SID>MWMoveNoRedirect(<f-args>)
command! -nargs=? MWWrite call <SID>MWWrite(<f-args>)
command! -nargs=? MWDiff call <SID>MWDiff(<f-args>)
command! -nargs=1 MWSearch call <SID>MWSearch(<f-args>)
command! -nargs=? MWSubpages call <SID>MWSubpages(<f-args>)
command! -nargs=? MWBrowse call <SID>MWBrowse(<f-args>)

augroup mediawiki
  autocmd!

  " Try to make mediawiki stuff automatically :w to the right place since we set 
  " the buftype=acwrite
  autocmd BufWriteCmd *.wiki call <SID>MWWrite()
augroup END
