A script to configure your linux machine by installing some useful packages for developers

builld-essential
git
tree
git-flow
vim
maven
supervisor
php : 'apache2', 'apache2-utils', 'libapache2-mod-fcgid', 'php-pear', 'phpVERSION', 'phpVERSION-dev', 'phpVERSION-common', 'phpVERSION-cli', 'phpVERSION-apcu', 'phpVERSION-xml',  'phpVERSION-curl', 'phpVERSION-fpm', 'php5.6-json', 'phpVERSION-opcache', 'phpVERSION-readline', 'libapache2-mod-phpVERSION', 'phpVERSION-mcrypt', 'phpVERSION-mysql', 'phpVERSION-zip', 'php-mbstring', 'php-sqlite3', 'php-xdebug', 'libpcre3-dev'
    where VERSION = 5.6 7.2 7.4
composer
ssh
gimp
curl
terminator
zsh
npm (yo, bower, gulp-cli, generator-angular, generator-jhipster)
vsftpd
apache2 
apache2-utils
java8
java11
java13
docker
docker-compose


# run
python3 install.py

# Output
 --- Packages and tools intaller ---
    1- Install utils packages
    2- Configure GIT
    3- Install PHP 5.6
    4- Install PHP 7.2
    5- Install PHP 7.4
    6- Configure Hosts
    7- Configure apache2
    8- Configure supervisor
    9- Install Java
    10- Install NPM modules
    11- Install Docker
    12- Install all
    13- Quit

    Your choice :
    
Your choice : 

# For PHP
After installing php use the command usePhp to switch php version on your system
## Example
usePhp 5.6 