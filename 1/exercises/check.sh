#!/bin/bash

file="$1"

if [ -f "$file" ]; then
 echo "$file存在，且为普通文件"
else
 echo "$file根本没有，给我拿好了啊！"
fi
