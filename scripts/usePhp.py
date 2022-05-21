#!/usr/bin/env python3

import sys, os

PHP_VERSIONS = ['7.4', '8.0']

version = sys.argv[1]
print ('Version to use:', version)
for v in PHP_VERSIONS:
    if v != version:
        print (' ------- Unlinking php@', v)
        os.system('brew unlink php@' + v)

os.system('brew link php@'+ version + ' --force')
os.system('echo > ~/.phprc')
os.system("echo 'export PATH=" + '"/opt/homebrew/opt/php@' + version + '/bin:$PATH"' + "'>> ~/.phprc")
os.system("echo 'export PATH=" + '"/opt/homebrew/opt/php@' + version + '/sbin:$PATH"' + "'>> ~/.phprc")
os.system('php -version')
os.system('brew services restart httpd')
