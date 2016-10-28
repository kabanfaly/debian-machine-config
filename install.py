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
                      "mysql-server", "php-mysql", "phpmyadmin", "php-sqlite3", "atool", "ipython", "python3-setuptools",
                      "ssh", "gimp")

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

    # Extra install
    resp = os.system("sudo easy_install3 pip")
    if resp != 0:
        status.append("Install pip .... KO")
    else:
        install_ok += 1
        total += 1
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


def run():

    os.system("sudo apt-get update")
    install_packages()
    configure_git()
    install_oracle_jdk()

if __name__ == '__main__':
    run()
