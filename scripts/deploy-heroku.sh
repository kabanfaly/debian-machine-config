#!/usr/bin/env zsh

if [ "$#" -ne 3 ]; then
    echo "3 arguments required: source app-name, heroku-app name and language (java|js) \n"
    echo "Usage: deploy-heroku.sh webscolaire webscolaire-app java"
    exit
fi

SOURCE_APP=$1
HEROKU_APP=$2
LANGUAGE=$3
LANGUAGE_DIR="Java"

if [ "$LANGUAGE" = "js" ]; then
  LANGUAGE_DIR="JS"
fi


WORKSPACE=/Users/nfalykaba/Workspace
SOURCE_DIR=$WORKSPACE/$LANGUAGE_DIR/$SOURCE_APP/
DEST_DIR=$WORKSPACE/heroku/$HEROKU_APP/

if [ ! -d "$SOURCE_DIR" ]; then
  echo "$SOURCE_DIR does not exist."
  exit
fi

if [ ! -d "$DEST_DIR" ]; then
 echo "$DEST_DIR does not exist."
 exit
fi

cd $DEST_DIR && rsync -av $SOURCE_DIR/*  $DEST_DIR/ --exclude 'dist' --exclude 'target' --exclude 'node_modules' --delete-before
git add .
git commit -am "deploy"
git push heroku main
cd -
