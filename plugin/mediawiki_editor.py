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

site = mwclient.Site(vim.eval('g:mediawiki_editor_url'))
site.login(vim.eval('g:mediawiki_editor_username'), vim.eval('g:mediawiki_editor_password'))

def mw_read(article_name):
    global site
    vim.current.buffer[:] = site.Pages[article_name].text().split("\n")
    vim.command('set ft=mediawiki')
    vim.command('setlocal buftype=nofile')
    vim.command('file! %s' % article_name)


def input(prompt, text=''):
    vim.command('call inputsave()')
    vim.command("let i = input('%s', '%s')" % (prompt, text))
    vim.command('call inputrestore()')
    return vim.eval('i')


def mw_write(article_name):
    if not article_name:
        article_name = vim.current.buffer.name.rsplit('/', 1)[1]
    else:
        article_name = article_name[0]

    global site
    page = site.Pages[article_name]
    summary = input('Edit summary: ')
    minor = input('Minor edit? [y/n]: ') == 'y'

    print

    result = page.save("\n".join(vim.current.buffer[:]), summary=summary, minor=minor)
    if result['result']:
        print 'Successfully edited %s.' % result['title']
    else:
        sys.stderr.write('Failed to edit %s.' % article_name)


def mw_diff(article_name):
    global site
    vim.command('diffthis')
    vim.command('leftabove split %s' % (article_name + '_diff'))
    vim.command('setlocal buftype=nofile')
    vim.command('diffthis')
    vim.command('set ft=mediawiki')
    vim.current.buffer[:] = site.Pages[article_name].text().split("\n")
    vim.command('set nomodifiable')


def mw_browse(article_name):
    pass
