#!/usr/bin/env bash

mkdir tmpdir
git clone --bare https://github.com/timelapseplus/VIEW.git tmpdir

pushd tmpdir
log=$(git log --date=iso \
    --since=`date --date='yesterday' +%Y-%m-%d` \
    --until=`date --date='tomorrow' +%Y-%m-%d` \
    --summary --show-notes --oneline --date-order)

echo "$log" >> "tmpFile.txt"
popd

rm -rf tmpdir

