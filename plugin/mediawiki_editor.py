import sys

try:
    import mwclient
except:
    sys.stderr.write('mwclient not installed; please install perhaps via pip install mwclient.')
    raise


from_cmdline = False
try:
    __file__
    from_cmdline = True
except NameError:
    pass


if not from_cmdline:
    import vim


def base_url():
    return vim.eval('g:mediawiki_editor_url')


def sq_escape(s):
    return s.replace("'", "''")


def fn_escape(s):
    return vim.eval("fnameescape('%s')" % sq_escape(s))


site = mwclient.Site(base_url())
site.login(vim.eval('g:mediawiki_editor_username'), vim.eval('g:mediawiki_editor_password'))


def mw_read(article_name):
    global site
    vim.current.buffer[:] = site.Pages[article_name].text().split("\n")
    vim.command('set ft=mediawiki')
    vim.command('setlocal buftype=nofile')
    vim.command("let b:article_name = '%s'" % sq_escape(article_name))
    vim.command('file! %s' % fn_escape(article_name))


def input(prompt, text=''):
    vim.command('call inputsave()')
    vim.command("let i = input('%s', '%s')" % (sq_escape(prompt), sq_escape(text)))
    vim.command('call inputrestore()')
    return vim.eval('i')


def infer_default(article_name):
    if not article_name:
        article_name = vim.current.buffer.vars.get('article_name')
    else:
        article_name = article_name[0]

    if not article_name:
        sys.stderr.write('No article specified.')

    return article_name


def mw_write(article_name):
    article_name = infer_default(article_name)

    global site
    page = site.Pages[article_name]
    summary = input('Edit summary: ')
    minor = input('Minor edit? [y/n]: ') == 'y'

    print ' '

    result = page.save("\n".join(vim.current.buffer[:]), summary=summary, minor=minor)
    if result['result']:
        print 'Successfully edited %s.' % result['title']
    else:
        sys.stderr.write('Failed to edit %s.' % article_name)


def mw_diff(article_name):
    article_name = infer_default(article_name)

    global site
    vim.command('diffthis')
    vim.command('leftabove split %s' % fn_escape(article_name + ' HEAD'))
    vim.command('setlocal buftype=nofile')
    vim.command('diffthis')
    vim.command('set ft=mediawiki')
    vim.current.buffer[:] = site.Pages[article_name].text().split("\n")
    vim.command('set nomodifiable')


def mw_browse(article_name):
    article_name = infer_default(article_name)

    url = 'http://%s/wiki/%s' % (base_url(), article_name)
    if not vim.eval("exists('g:loaded_netrw')"):
        vim.command('runtime! autoload/netrw.vim')

    if int(vim.eval("exists('*netrw#BrowseX')")):
        vim.command("call netrw#BrowseX('%s', 0)" % sq_escape(url))
    else:
        vim.command("call netrw#NetrwBrowseX('%s', 0)" % sq_escape(url))
