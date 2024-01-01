#! /bin/bash

set -e

read -p "api gateway url? : " url
if [[ -z "$url" ]]; then
  echo "url is blank." >2
  exit
fi

export URL=$url
