import os
from config import *


def configure_git():
    print('----- Configuring GIT -----')

    confirm = input('Your are about to configure git. Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
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

    # Extra installation
    # - pip installation
    total += 1
    resp = os.system("sudo easy_install3 pip")
    if resp != 0:
        status.append("Install pip .... KO")
    else:
        install_ok += 1
        os.system("sudo pip install --upgrade pip")
        status.append("Install pip .... OK")

    print("---- End of packages installation  ----")

    for s in status:
        print(s)
    print("Report: %d/%d packages installed" % (install_ok, total))

def install_utils_packages():
    """
    Install some utilities packages
    :return:
    """
    confirm = input('Your are about to install utils packages. Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
        install_packages(UTILS_PACKAGES)

def install_php5_6():
    """
    Install some php packages
    :return:
    """
    confirm = input('Your are about to install php 5.6 . Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
        os.system('sudo apt install software-properties-common')
        os.system('sudo add-apt-repository ppa:ondrej/php && sudo apt update')
        install_packages(PHP5_6_PACKAGES)

def install_php7_2():
    """
    Install some php packages
    :return:
    """
    confirm = input('Your are about to install php 7.2 . Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
        os.system('sudo apt install software-properties-common')
        os.system('sudo add-apt-repository ppa:ondrej/php && sudo apt update')
        install_packages(PHP7_2_PACKAGES)

def install_php7_4():
    """
    Install some php packages
    :return:
    """
    confirm = input('Your are about to install php 7.4 . Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
        os.system('sudo apt install software-properties-common')
        os.system('sudo add-apt-repository ppa:ondrej/php && sudo apt update')
        install_packages(PHP7_4_PACKAGES)

def install_java():
    """
    Install oracle version of JDK11 and JDK13
    :return:
    """
    print('----- Installing Java -----')

    confirm = input('Your are about to install java. Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
        os.system("sudo apt-get install -y software-properties-common")
        os.system("add-apt-repository ppa:linuxuprising/java")
        os.system("sudo apt-get update")
        os.system("sudo apt-get install -y openjdk-8-jdk openjdk-11-jdk openjdk-13-jdk openjdk-14-jdk oracle-java11-installer oracle-java13-installer")

        print("Installing java-11 and java13 OK ...")


def install_npm_modules():
    """
    Install some npm modules
    :return:
    """
    print('----- Installing npm modules -----')

    confirm = input('Your are about to install npm modules. Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
        os.system("sudo apt-get update")
        os.system("sudo apt-get install -y npm")
        os.system("sudo ln -sf /usr/bin/nodejs /usr/bin/node")
        modules = ["npm", "yo", "gulp-cli", "bower", "generator-angular", "generator-jhipster"]

        for mod in modules:
            os.system("sudo npm install -g %s" % mod)

        os.system("sudo apt remove nodejs npm")
        os.system("curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -")
        os.system("sudo apt-get install -y nodejs")


def configure_hosts():
    """
    add costum hosts
    :return:
    """
    print('----- Configuring hosts -----')

    confirm = input('Your are about to configure hosts. Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
        if 'dev.perform-world.com' not in open('/etc/hosts').read():
            os.system("echo  '127.0.0.1       dev.perform-world.com' | sudo tee -a /etc/hosts")
            os.system("echo  '127.0.0.1       local.supervisor' | sudo tee -a /etc/hosts")


def configure_apache2():
    """
    configures apache2
    :return:
    """
    print('----- Configuring apache2 -----')
    confirm = input('Your are about to configure apache2. Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
        os.system('sudo apt install apache2')
        os.system("sudo cp ./apache2/sites-available/perform-world.conf /etc/apache2/sites-available")
        os.system("sudo a2enmod proxy")
        os.system("sudo service apache2 restart")
        os.system("sudo a2ensite perform-world.conf")
        os.system('sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
        os.system("sudo chmod +x /usr/local/bin/docker-compose")

def install_docker():
    """
    Install docker
    """
    print('----- Installing docker -----')
    confirm = input('Your are about to install docker. Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
        os.system("sudo apt-get update")
        os.system("sudo apt-get remove docker docker-engine docker.io")
        os.system("sudo apt install -y docker.io")
        os.system("sudo systemctl start docker")
        os.system("sudo systemctl enable docker")
        print('----- Installing docker-compose -----')
        os.system('sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
        os.system('sudo chmod +x /usr/local/bin/docker-compose')
        os.system('sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')
        os.system('docker-compose --version')

def configure_supervisor():

    """
    configures supervisord
    :return:
    """
    print('----- Installing supervisor -----')

    confirm = input('Your are about to install supervisor. Do you want to continue ? Y/N : ')
    if confirm.upper() in ('Y', 'YES') :
        os.system("sudo apt-get update")
        os.system("sudo apt install -y supervisor")
        os.system("sudo cp ./apache2/sites-available/supervisord.conf /etc/apache2/sites-available")

        if 'kaba' not in open('/etc/hosts').read():
            os.system("echo  '[inet_http_server]' | sudo tee -a /etc/supervisor/supervisord.conf")
            os.system("echo  'port = 127.0.0.1:9001' | sudo tee -a /etc/supervisor/supervisord.conf")
            os.system("echo  'username = kaba' | sudo tee -a /etc/supervisor/supervisord.conf")
            os.system("echo  'password = {SHA}da3c01ea4729ba5fc5ed83d2e85b2b00c118753f' | sudo tee -a /etc/supervisor/supervisord.conf")

        os.system("sudo a2ensite supervisord.conf")
        os.system("sudo service apache2 restart")
        os.system("sudo service supervisor restart")

def install_all():
    install_utils_packages()
    configure_git()
    install_php5_6()
    install_php7_2()
    install_php7_4()
    configure_hosts()
    configure_apache2()
    configure_supervisor()
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
    6- Configure Hosts
    7- Configure apache2
    8- Configure supervisor
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
        6: configure_hosts,
        7: configure_apache2,
        8: configure_supervisor,
        9: install_java,
        10: install_npm_modules,
        11: install_docker,
        12: install_all,
        13: quit
    }

    choice_resolver[choice]()

if __name__ == '__main__':
    run()
