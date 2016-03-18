#!/bin/bash

NAME=${1:-rendered}
FPS=${2:-24}
DIRECTORY=export
# JPEG=${3:-false}

function count {
    ls *.CR2 -l | wc -l
}

function export() {
    for i in $( ls *.CR2 ); do
        darktable-cli $i $i.xmp $DIRECTORY/$i.jpg
        printf 1++"/"$1
    done
}

# create file list
function listFiles {
    ls -v export | grep jpg > $DIRECTORY/files.txt
}

# render
function render () {
    cd $DIRECTORY && mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=21600000 -o ~/Videos/$1.avi -mf type=jpeg:fps=$2 mf://@files.txt -vf scale=1920:1080
    notify-send -t 5000 "Your timelapse has finished rendering and is located in ~/Videos"
}

function cleanup {
    cp rendered.avi . && cd .
    rm -r export
}

# exit program
function quit {
exit
}

# jpeg deflicker

function jpegDeflicker {
    ./home/gabeduke/repos/timelapse-scripts/perl/deflicker.pl -v
    $DIRECTORY=Deflicker
}

if [ ! -d "$DIRECTORY" ]; then
  export count
  listFiles
  if [ ! $JPEG = "false" ]; then
      jpegDeflicker
  fi
  render $NAME $FPS
  quit
else
  render $NAME $FPS
  quit
fi
