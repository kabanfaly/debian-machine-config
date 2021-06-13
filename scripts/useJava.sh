#!/usr/bin/env zsh

JDK_NAME=$1

if [ -z "$JDK_NAME" ]
then
  echo "Invalid parameter: Please use any jkd name located in /usr/lib/jvm/"
  echo "Example of usage: \nuseJava adopt-openjdk-11.0.11"
  exit
fi
sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/$JDK_NAME/bin/java" 0
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/$JDK_NAME/bin/javac" 0
sudo update-alternatives --set java /usr/lib/jvm/$JDK_NAME/bin/java
sudo update-alternatives --set javac /usr/lib/jvm/$JDK_NAME/bin/javac
update-alternatives --list java
update-alternatives --list javac

export JAVA_HOME=/usr/lib/jvm/$JDK_NAME
