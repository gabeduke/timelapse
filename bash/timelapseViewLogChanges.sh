#!/usr/bin/env bash

key='35415ce80659263baf97541ef623ecc28de9ea714a8c1d2c'
application='Timelapse View Notifier'

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

. resty/resty -W 'https://www.notifymyandroid.com'

POST /publicapi/notify "apikey=${key}" -d "application=${application}" -d "event=COMMITS" -d "description=${log}"