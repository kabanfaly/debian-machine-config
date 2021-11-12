import os
from config import *


def configure_git():
    print('----- Configuring GIT -----')

    confirm = input('Your are about to configure git. Do you want to continue ? [Y/n] : ')
    if confirm.upper() not in ('N', 'No'):
        resp1 = os.system("git config --global user.email \"%s\"" % CONFIG["email"])
        resp2 = os.system("git config --global user.name \"%s\"" % CONFIG["name"])

        if resp1 + resp2 == 0:
            print("git configuration .... OK")
        else:
            print("git configuration .... KO")


def install_packages(packages):
    """
    Install useful packages
    :return:
    """
    status = []
    install_ok = 0  # number of installed packages
    total = len(packages)  # number of packages to install

    print("---- Starting packages installation  ----")
    os.system("sudo apt-get update")

    for package in packages:
        resp = os.system("sudo apt-get install %s -y" % package)

        # set installation status
        if resp != 0:
            status.append("Install %s .... KO" % package)
        else:
            install_ok += 1
            status.append("Install %s .... OK" % package)

    print("---- End of packages installation  ----")

    for s in status:
        print(s)
    print("Report: %d/%d packages installed" % (install_ok, total))


def install_utils_packages():
    """
    Install some utilities packages
    :return:
    """
    confirm = input('Your are about to install utils packages. Do you want to continue ? [Y/n] : ')
    if confirm.upper() not in ('N', 'No'):
        install_packages(UTILS_PACKAGES)


def install_php(version):
    """
    Install some php packages
    :return:
    """
    confirm = input('Your are about to install php ' + version + ' . Do you want to continue ? [Y/n] : ')
    if confirm.upper() not in ('N', 'No'):
        os.system('sudo apt install software-properties-common')
        os.system('sudo add-apt-repository ppa:ondrej/php && sudo apt update')
        packages = [package.replace('VERSION', version) for package in PHP_PACKAGES]
        install_packages(packages)
        os.system('sudo a2enmod actions alias proxy_fcgi fcgid')
        os.system('echo echo "<?php phpinfo() ?>" | sudo tee /var/www/html/_info.php')
        os.system('sudo cp ./scripts/usePhp.py /usr/local/bin')
        os.system('sudo mv /usr/local/bin/usePhp.py /usr/local/bin/usePhp')
        os.system('sudo chmod +x /usr/local/bin/usePhp')

        install_composer()
        os.system('sudo systemctl restart apache2')
        print('php ' + version + ' is completely installed. Use the command "usePhp" to switch php version.\n')
        print('Example: usePhp ' + version)


def install_composer():
    """
    Install some php composer
    :return:
    """
    print('Installing composer ....')
    os.system('sudo apt install curl')
    os.system('curl -sS https://getcomposer.org/installer -o composer.php')
    os.system('HASH=`curl -sS https://composer.github.io/installer.sig`')
    os.system('echo $HASH')
    os.system(
        "php -r \"if (hash_file('SHA384', 'composer.php') === '$HASH') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;\"")
    os.system('sudo php composer.php --install-dir=/usr/local/bin --filename=composer')


def install_php5_6():
    install_php('5.6')


def install_php7_2():
    install_php('7.2')


def install_php7_4():
    install_php('7.4')


def install_java():
    """
    Install oracle version of JDK11 and JDK13
    :return:
    """
    print('----- Installing Java -----')

    confirm = input('Your are about to install java. Do you want to continue ? [Y/n] : ')
    if confirm.upper() not in ('N', 'No'):
        print('----- Installing sdkman -----')
        os.system('curl -s "https://get.sdkman.io" | bash')
        print('----- Run the following commands to complete java installation -----')
        print('source "$HOME/.sdkman/bin/sdkman-init.sh"')
        print('sdk list java')
        print('sdk install java 11.0.11.j9-adpt')
        print('sdk install java 16.0.1.j9-adpt')
        print('sdk install java 8.0.292.j9-adpt')
        print('----- sdkman installation done -----')   


def install_npm_modules():
    """
    Install some npm modules
    :return:
    """
    print('----- Installing npm modules -----')

    confirm = input('Your are about to install npm modules. Do you want to continue ? [Y/n] : ')
    if confirm.upper() not in ('N', 'No'):
        os.system("sudo apt remove -y nodejs npm")
        os.system("curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -")
        os.system("sudo apt-get update")
        os.system("sudo apt-get install -y nodejs")
        print('------- Installing npm modules --------')

        for mod in NPM_MODULES:
            os.system("sudo npm install -g %s" % mod)
        print("run: 'sudo dpkg -r --force-depends nodejs' if the installation fails")


def configure_hosts():
    """
    add custom hosts
    :return:
    """
    print('----- Configuring hosts -----')

    confirm = input('Your are about to configure hosts. Do you want to continue ? [Y/n] : ')
    if confirm.upper() not in ('N', 'No'):
        if 'dev.perform-world.com' not in open('/etc/hosts').read():
            os.system("echo  '127.0.0.1       dev.perform-world.com' | sudo tee -a /etc/hosts")
            os.system("echo  '127.0.0.1       local.supervisor' | sudo tee -a /etc/hosts")


def configure_apache2():
    """
    configures apache2
    :return:
    """
    print('----- Configuring apache2 -----')
    confirm = input('Your are about to configure apache2. Do you want to continue ? [Y/n] : ')
    if confirm.upper() not in ('N', 'No'):
        os.system('sudo apt install apache2')
        os.system("sudo cp ./apache2/sites-available/perform-world.conf /etc/apache2/sites-available")
        os.system("sudo a2enmod proxy")
        os.system("sudo service apache2 restart")
        os.system("sudo a2ensite perform-world.conf")


def install_docker():
    """
    Install docker
    """
    print('----- Installing docker -----')
    confirm = input('Your are about to install docker. Do you want to continue ? [Y/n] : ')
    if confirm.upper() not in ('N', 'No'):
        os.system("sudo apt-get update")
        os.system("sudo apt-get remove docker docker-engine docker.io")
        os.system("sudo apt install -y docker.io")
        os.system("sudo systemctl start docker")
        os.system("sudo systemctl enable docker")
        print('----- Installing docker-compose -----')
        os.system(
            'sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
        os.system('sudo chmod +x /usr/local/bin/docker-compose')
        os.system('sudo chmod 666 /var/run/docker.sock')
        os.system('sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')
        os.system('docker-compose --version')


def configure_supervisor():
    """
    configures supervisord
    :return:
    """
    print('----- Installing supervisor -----')

    confirm = input('Your are about to install supervisor. Do you want to continue ? [Y/n] : ')
    if confirm.upper() not in ('N', 'No'):
        os.system("sudo apt-get update")
        os.system("sudo apt install -y supervisor")
        os.system("sudo cp ./apache2/sites-available/supervisord.conf /etc/apache2/sites-available")

        if 'kaba' not in open('/etc/hosts').read():
            os.system("echo  '[inet_http_server]' | sudo tee -a /etc/supervisor/supervisord.conf")
            os.system("echo  'port = 127.0.0.1:9001' | sudo tee -a /etc/supervisor/supervisord.conf")
            os.system("echo  'username = kaba' | sudo tee -a /etc/supervisor/supervisord.conf")
            os.system(
                "echo  'password = {SHA}da3c01ea4729ba5fc5ed83d2e85b2b00c118753f' | sudo tee -a /etc/supervisor/supervisord.conf")

        os.system("sudo a2ensite supervisord.conf")
        os.system("sudo service apache2 restart")
        os.system("sudo service supervisor restart")


def install_all():
    install_utils_packages()
    configure_git()
    install_php5_6()
    install_php7_2()
    install_php7_4()
    #configure_hosts()
    #configure_apache2()
    #configure_supervisor()
    install_java()
    install_npm_modules()
    install_docker()


def run():
    menu = '''
    --- Packages and tools intaller ---
    1- Install utils packages
    2- Configure GIT
    3- Install PHP 5.6
    4- Install PHP 7.2
    5- Install PHP 7.4
    #6- Configure Hosts (ignored)
    #7- Configure apache2 (ignored)
    #8- Configure supervisor (ignored)
    9- Install Java
    10- Install NPM modules
    11- Install Docker
    12- Install all
    13- Quit

    Your choice :
    '''
    print(menu)
    choice = int(input('Your choice : '))

    choice_resolver = {
        1: install_utils_packages,
        2: configure_git,
        3: install_php5_6,
        4: install_php7_2,
        5: install_php7_4,
        #6: configure_hosts,
        #7: configure_apache2,
        #8: configure_supervisor,
        9: install_java,
        10: install_npm_modules,
        11: install_docker,
        12: install_all,
        13: quit
    }

    choice_resolver[choice]()


if __name__ == '__main__':
    run()
