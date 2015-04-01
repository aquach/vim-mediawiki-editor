import mwclient

from_cmdline = False
try:
    __file__
    from_cmdline = True
except NameError:
    pass

if not from_cmdline:
    import vim

site = mwclient.Site(vim.eval('g:mediawiki_editor_url'))
site.login(vim.eval('g:mediawiki_editor_username'), vim.eval('g:mediawiki_editor_password'))

def mw_read(article_name):
    global site
    vim.current.buffer[:] = site.Pages[article_name].text().split("\n")
    vim.command('set ft=mediawiki')
    vim.comand('file! %s' % article_name)


def mw_write(article_name):
    pass


def mw_diff(article_name):
    pass
