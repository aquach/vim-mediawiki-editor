# vim-mediawiki-editor

Edit MediaWiki articles from the comfort of Vim, your favorite text editor!

<p align="center">
  <img src="https://raw.githubusercontent.com/aquach/vim-mediawiki-editor/master/examples/demo.gif">
</p>

## Installation

vim-mediawiki-editor requires Vim compiled with python support and the [python `mwclient` library](https://github.com/mwclient/mwclient).

You likely have Python support, but you can check with `vim --version | grep +python`. MacVim comes with Python support.

If you get an error, try `pip install mwclient` to get the library.

Once you have these, use your favorite Vim plugin manager to install `aquach/vim-mediawiki-editor`, or copy `plugin` and `doc` into your `.vim` folder.

I recommend pairing this plugin with [mediawiki.vim](https://github.com/chikamichi/mediawiki.vim) for syntax highlighting and with [goyo.vim](https://github.com/junegunn/goyo.vim) for WriteRoom-esque editing.

## Usage

vim-mediawiki-editor offers these commands:

#### :MWRead <article-name>

Loads the given article into the current buffer.

```
:MWRead Radish
```

#### :MWWrite [article-name]

Writes the buffer back to the site. If you don't specify an article name, it defaults to the article you currently have open with `:MWRead`. After prompting you for the edit summary and major/minor edit, it will publish your work back to the site.

#### :MWDiff [article-name]

Diffs the current buffer against the hosted version of the article specified on the site. If you don't specify an article name, it defaults to the article you currently have open with `:MWRead`.

#### :MWBrowse [article-name]

Views the article specified in your configured browser. If you don't specify an article name, it defaults to the article you currently have open with `:MWRead`.

## Configuration

If you don't specify these settings, vim-mediawiki-editor will prompt you when you first run a vim-mediawiki-editor command.

#### g:mediawiki_editor_url

The URL of the site you're editing. For the English wikipedia, that'd be `en.wikipedia.org`.

#### g:mediawiki_editor_path

The MediaWiki [script path](https://www.mediawiki.org/wiki/Manual:$wgScriptPath).
For the wikipedias and other WMF wikis, this is `/w/`, but for other wikis it can be `/`, `/wiki/`,
or some other value.

#### g:mediawiki_editor_username

Your account username.

#### g:mediawiki_editor_password

Your account password. I recommend putting the URL and username in your `.vimrc` and letting Vim ask for your password.

#### g:mediawiki_basicauth_enabled

Set this to `on` to enable HTTP Basic Authentication.

#### g:mediawiki_basicauth_username

The HTTP Basic Auth Username. Will be prompted if not provided and basic `g:mediawiki_basicauth_enabled` is on.

#### g:mediawiki_basicauth_password

The HTTP Basic Auth Password. Will be prompted if not provided and basic `g:mediawiki_basicauth_enabled` is on.

## Contributing

This plugin is currently quite simple. Contributions, suggestions, and feedback are all welcomed!
