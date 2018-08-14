#!/usr/bin/env bash
a="one,two,three,four"
arr=($a)
IFS=","
for s in ${arr[@]}
do
    echo "$s"
done