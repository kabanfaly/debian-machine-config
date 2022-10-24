#!/usr/bin/env python3

import sys, os

PHP_VERSIONS = ['7.4', '8.0']

version = sys.argv[1]
print ('Version to use:', version)

os.system('brew-php-switcher '+ version)
os.system('echo > ~/.phprc')
os.system("echo 'export PATH=" + '"/opt/homebrew/opt/php@' + version + '/bin:$PATH"' + "'>> ~/.phprc")
os.system("echo 'export PATH=" + '"/opt/homebrew/opt/php@' + version + '/sbin:$PATH"' + "'>> ~/.phprc")
os.system('brew services restart httpd')
os.system('php -version')