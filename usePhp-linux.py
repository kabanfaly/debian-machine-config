#!/usr/bin/env python3

import sys, os

PHP_VERSIONS = ['5.6', '7.2', '7.4']

version = sys.argv[1]
print ('Version to use:', version)
for v in PHP_VERSIONS:
    if v != version:
        print (' ------- Disabling mod php', v)
        os.system('sudo a2dismod php' + v)
        print (' ------- Disabling conf php', v)
        os.system('sudo a2disconf php' + v + '-fpm.conf')

os.system('sudo a2dismod php' + version)
os.system('sudo a2enconf php' + version + '-fpm.conf')
alternative = 'sudo update-alternatives --set php /usr/bin/php' + version
os.system(alternative)
os.system('sudo service php' + version + '-fpm start')
os.system('sudo service apache2 restart')
os.system('php -version')
