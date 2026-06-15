#!/usr/bin/env python3

import sys, os

PHP_VERSIONS = ['7.4', '8.2', '8.3']

version = sys.argv[1]
print ('Version to use:', version)

os.system('brew-php-switcher '+ version)
os.system('echo > ~/.phprc')
os.system("echo 'export PATH=" + '"/opt/homebrew/opt/php@' + version + '/bin:$PATH"' + "'>> ~/.phprc")
os.system("echo 'export PATH=" + '"/opt/homebrew/opt/php@' + version + '/sbin:$PATH"' + "'>> ~/.phprc")
os.system('export LDFLAGS="-L/opt/homebrew/opt/php@' + version + '/lib"')
os.system('export CPPFLAGS="-I/opt/homebrew/opt/php@' + version +'/include"')
os.system('brew services restart php@' + version)
os.system('brew services restart httpd')
os.system('php -version')
