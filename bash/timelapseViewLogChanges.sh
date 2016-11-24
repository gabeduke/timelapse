#!/usr/bin/env bash

mkdir tmpdir
git clone --bare https://github.com/timelapseplus/VIEW.git tmpdir
pushd tmpdir
log=$(git log --date=iso \
    --since=`date --date='yesterday' +%Y-%m-%d` \
    --until=`date --date='tomorrow' +%Y-%m-%d` \
    --summary --show-notes --oneline --date-order)
popd
rm -rf tmpdir
echo "$log" >> "tmpFile.txt"
mutt -s "Timelapse VIEW Log Changes" gabeduke@gmail.com < tmpFile.txt
rm tmpFile.txt