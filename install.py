import os
from config import CONFIG


def configure_git():
    resp1 = os.system("git config --global user.email \"%s\"" % CONFIG["email"])
    resp2 = os.system("git config --global user.name \"%s\"" % CONFIG["name"])

    if resp1 + resp2 == 0:
        print("git configuration .... OK")
    else:
        print("git configuration .... KO")


def install_packages():
    """
    Install useful packages
    :return:
    """
    utils_packages = ("build-essential", "git", "tree", "git-flow", "vim", "maven", "supervisor", "php", "libapache2-mod-php", "apache2", "php-mcrypt",
                      "mysql-server", "php-mysql", "phpmyadmin", "php-sqlite3", "atool", "ipython", "python3-setuptools", "python3-mysqldb",
                      "ssh", "gimp", "curl", "terminator", "zsh", "npm")

    status = []

    install_ok = 0  # number of installed packages

    total = len(utils_packages)  # number of packages to install

    print("---- Starting packages installation  ----")
    for package in utils_packages:
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


# Installing JDK7 JDK8
def install_oracle_jdk():
    """
    Install oracle version of JDK7 and JDK8
    :return:
    """
    os.system("sudo apt-get install -y python-software-properties")
    os.system("sudo add-apt-repository ppa:webupd8team/java")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y oracle-java7-installer oracle-java8-installer")

    print("Installing Java7 OK ...")


def install_npm_modules():
    """
    Install some npm modules
    :return:
    """
    os.system("sudo ln -sf /usr/bin/nodejs /usr/bin/node")
    modules = ["npm", "yo", "gulp-cli", "bower", "generator-jhipster"]

    for mod in modules:
        os.system("sudo npm install -g %s" % mod)


def configure_hosts():
    """
    add costum hosts
    :return:
    """
    if 'dev.perform-world.com' not in open('/etc/hosts').read():
        os.system("echo  '127.0.0.1       dev.perform-world.com' | sudo tee -a /etc/hosts")
        os.system("echo  '127.0.0.1       local.supervisor' | sudo tee -a /etc/hosts")


def configure_apache2():
    """
    configures apache2
    :return:
    """
    os.system("sudo cp ./apache2/sites-available/perform-world.conf /etc/apache2/sites-available")
    os.system("sudo a2ensite perform-world.conf")
    os.system("sudo service apache2 restart")



def configure_supervisor():
    """
    configures supervisord
    :return:
    """

    os.system("sudo cp ./apache2/sites-available/supervisord.conf /etc/apache2/sites-available")

    if 'kaba' not in open('/etc/hosts').read():
        os.system("echo  '[inet_http_server]' | sudo tee -a /etc/supervisor/supervisord.conf")
        os.system("echo  'port = 127.0.0.1:9001' | sudo tee -a /etc/supervisor/supervisord.conf")
        os.system("echo  'username = kaba' | sudo tee -a /etc/supervisor/supervisord.conf")
        os.system("echo  'password = {SHA}da3c01ea4729ba5fc5ed83d2e85b2b00c118753f' | sudo tee -a /etc/supervisor/supervisord.conf")

    os.system("sudo a2ensite supervisord.conf")
    os.system("sudo service apache2 restart")
    os.system("sudo service supervisor restart")

def run():

    os.system("sudo apt-get update")
    install_packages()
    configure_git()
    install_oracle_jdk()
    install_npm_modules()
    configure_hosts()
    configure_apache2()
    # configure_supervisor()

if __name__ == '__main__':
    run()
