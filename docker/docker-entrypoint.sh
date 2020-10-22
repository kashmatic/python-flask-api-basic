#!/bin/sh

set -e

flask db init
ls -l
if [ -e migrations ]
then
  flask db migrate
else
  echo "migrations dir present"
fi
flask db upgrade
