import sys

try:
    import mwclient
except ImportError:
    sys.stderr.write(
            'mwclient not installed; install perhaps via'
            ' pip install mwclient.\n')
    raise


from_cmdline = False
try:
    __file__
    from_cmdline = True
except NameError:
    pass


if not from_cmdline:
    import vim


# Utility.

def sq_escape(s):
    return s.replace("'", "''")


def fn_escape(s):
    return vim.eval("fnameescape('%s')" % sq_escape(s))


def input(prompt, text=''):
    vim.command('call inputsave()')
    vim.command("let i = input('%s', '%s')" % (sq_escape(prompt),
        sq_escape(text)))
    vim.command('call inputrestore()')
    return vim.eval('i')


def var_exists(var):
    return bool(int(vim.eval("exists('%s')" % sq_escape(var))))


def get_from_config_or_prompt(var, prompt):
    if var_exists(var):
        return vim.eval(var)
    else:
        resp = input(prompt)
        vim.command("let %s = '%s'" % (var, sq_escape(resp)))
        return resp


def base_url():
    return get_from_config_or_prompt('g:mediawiki_editor_url',
            "Mediawiki URL, like 'en.wikipedia.org': ")


def site():
    if site.cached_site:
        return site.cached_site

    s = mwclient.Site(base_url())
    try:
        s.login(
                get_from_config_or_prompt('g:mediawiki_editor_username',
                    'Mediawiki Username: '),
                get_from_config_or_prompt('g:mediawiki_editor_password',
                    'Mediawiki Password: ')
                )
    except mwclient.errors.LoginError as e:
        sys.stderr.write('Error logging in: %s\n' % e)
        vim.command(
                'unlet g:mediawiki_editor_username '
                'g:mediawiki_editor_password'
                )
        raise

    site.cached_site = s
    return s

site.cached_site = None


def infer_default(article_name):
    if not article_name:
        article_name = vim.current.buffer.vars.get('article_name')
    else:
        article_name = article_name[0]

    if not article_name:
        sys.stderr.write('No article specified.\n')

    return article_name


# Commands.

def mw_read(article_name):
    s = site()
    vim.current.buffer[:] = s.Pages[article_name].text().split("\n")
    vim.command('set ft=mediawiki')
    vim.command("let b:article_name = '%s'" % sq_escape(article_name))


def mw_write(article_name):
    article_name = infer_default(article_name)

    s = site()
    page = s.Pages[article_name]
    summary = input('Edit summary: ')
    minor = input('Minor edit? [y/n]: ') == 'y'

    print ' '

    result = page.save("\n".join(vim.current.buffer[:]), summary=summary,
            minor=minor)
    if result['result']:
        print 'Successfully edited %s.' % result['title']
    else:
        sys.stderr.write('Failed to edit %s.\n' % article_name)


def mw_diff(article_name):
    article_name = infer_default(article_name)

    s = site()
    vim.command('diffthis')
    vim.command('leftabove vsplit %s' % fn_escape(article_name + ' - REMOTE'))
    vim.command('setlocal buftype=nofile bufhidden=delete nobuflisted')
    vim.command('set ft=mediawiki')
    vim.current.buffer[:] = s.Pages[article_name].text().split("\n")
    vim.command('diffthis')
    vim.command('set nomodifiable')


def mw_browse(article_name):
    article_name = infer_default(article_name)

    url = 'http://%s/wiki/%s' % (base_url(), article_name)
    if not var_exists('g:loaded_netrw'):
        vim.command('runtime! autoload/netrw.vim')

    if var_exists('*netrw#BrowseX'):
        vim.command("call netrw#BrowseX('%s', 0)" % sq_escape(url))
    else:
        vim.command("call netrw#NetrwBrowseX('%s', 0)" % sq_escape(url))
