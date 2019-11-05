if exists("b:did_ftplugin")
  finish
endif
let b:did_ftplugin = 1

" Useful mappings
nnoremap <nowait><buffer><silent> g. :MWBrowse<CR>
nnoremap <nowait><buffer><silent> g/ :MWSubpages<CR>
nnoremap <nowait><buffer><silent> gf "wyi[:MWRead <C-R>w<CR>
nnoremap <nowait><buffer><silent> <C-w>f "wyi[<C-w>n:MWRead <C-R>w<CR>
nnoremap <nowait><buffer><silent> gL "wyi[:MWBacklinks <C-R>w<CR>
nnoremap <nowait><buffer><silent> gl :MWBacklinks<CR>
vnoremap <nowait><buffer><silent> gf "wy:MWRead <C-R>w<CR>
vnoremap <nowait><buffer><silent> <C-w>f "wy<C-w>n:MWRead <C-R>w<CR>
vnoremap <nowait><buffer><silent> gs "wy:MWSearch <C-R>w<CR>
vnoremap <nowait><buffer><silent> <C-w>s "wy<C-w>n:MWSearch <C-R>w<CR>

nnoremap <buffer><silent> g?    :help mediawiki-editor-mappings<CR>



