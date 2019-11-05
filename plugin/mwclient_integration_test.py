import json
import sys
import mediawiki_editor

d = json.loads(sys.stdin.read())
username = d['username']
password = d['password']

mediawiki_editor.get_logged_in_client(
    uri_scheme='https',
    base_url='en.wikipedia.org',
    mediawiki_path='/w/',
    domain=None,
    basic_auth_creds=None,
    username=username,
    password=password,
)

print("Test passed.")
