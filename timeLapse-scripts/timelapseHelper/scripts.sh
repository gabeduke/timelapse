#!/usr/bin/env bash

# Script Parameters
NAME=${1:-rendered}
FPS=${2:-24}
QUALITY=${3:-normal}
DIRECTORY=$(pwd)
EXPORT=$DIRECTORY/export

function export () {
TOTAL="$(ls *.CR2 -l | wc -l)"
    for i in $( ls *.CR2 ); do
        darktable-cli $i $i.xmp $EXPORT/$i.jpg
        COUNTER=$((COUNTER+1))
        printf "%s/%s\n" "$COUNTER" "$TOTAL"
    done
}

function renderJpegs () {
    ls -1v | grep -E 'JPG|JPEG|jpeg|jpg' > files.txt mencoder -nosound -ovc lavc -lavcopts $LAVCOPTS -o ~/Videos/$NAME.avi -mf type=jpeg:fps=$FPS mf://@files.txt -vf scale=1920:1080
    notify-send -t 5000 "Your timelapse has finished rendering"}
}

# create file list
function listFiles () {
    ls -1v $EXPORT | grep -E 'JPG|JPEG|jpeg|jpg'  > $EXPORT/files.txt
}

function render () {
    cd $EXPORT && mencoder -nosound -ovc lavc -lavcopts $LAVCOPTS -o ~/Videos/$NAME.avi -mf type=jpeg:fps=$FPS mf://@files.txt -vf scale=1920:1080
    notify-send -t 5000 "Your timelapse has finished rendering"
}

function cleanup {
    cp rendered.avi . && cd .
    rm -r export
}

# TODO
# jpeg deflicker
function jpegDeflicker {
    ./home/gabeduke/repos/timelapse-scripts/perl/deflicker.pl -v
    $DIRECTORY=Deflicker
}

# TODO
function motionBlur {
    mogrify -verbose -limit memory 8192 *.jpg -delay 10 -morph 5
}