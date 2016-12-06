#!/bin/bash

# Script Parameters
NAME=${1:-rendered}
FPS=${2:-24}
QUALITY=${3:-normal}
DIRECTORY=$(pwd)
EXPORT=$DIRECTORY/export

# Menu variables
QUIT="Save & Continue"
SET_NAME="Set Title"
NAME_PROMPT="Enter new Timelapse Title (Current title is $NAME): "
SET_FPS="Set FPS"
FPS_PROMPT="Enter new FPS value (Current value is $FPS: "
SET_QUALITY="Set Quality"
QUALITY_PROMPT="Set new Quality (valid options are high and low): "
SET_DIR="Set target Directory"
DIR_PROMPT="Set target directory (Current path is $DIRECTORY): "
#SET_2PASS="Enable 2-Pass JPEG Deflickering"
#SET_MOGRIFY="Set Mogrify Value"
options=("$QUIT" "$SET_NAME" "$SET_FPS" "$SET_QUALITY" "$SET_DIR")
PS3='Please select a menu option (1  to continue): '

# This section sets the render quality
LAVCOPTS="vcodec=mpeg4:vbitrate=21600000"
#if [ $3 = "high" ]; then
# TODO check syntax
#    LAVCOPTS=$LAVCOPTS+":trell:mbd=2:dc=10"
#    fi

# first totals the number of files then exports
# each RAW image using darktable-cli while incrementing
# the counter and comparing to the total variable above
function export() {
TOTAL="$(ls *[.CR2][.cr2]* -l | wc -l)"
    for i in $( ls *[.CR2][.cr2]* ); do
        darktable-cli $i $i.xmp $EXPORT/$i.jpg
        COUNTER=$((COUNTER+1))
        printf "%s/%s\n" "$COUNTER" "$TOTAL"
    done
}

# create file list
function listFiles {
    ls -v $EXPORT | grep jpg > $EXPORT/files.txt
}

# render
function render () {
    cd $EXPORT && mencoder -nosound -ovc lavc -lavcopts $LAVCOPTS -o ~/Videos/$NAME.avi -mf type=jpeg:fps=$FPS mf://@files.txt -vf scale=1920:1080
    notify-send -t 5000 "Your timelapse has finished rendering"
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

###################################################################
# Variable Menu
###################################################################
echo $PS3
select opt in "${options[@]}"
do
    case $opt in
        $SET_NAME)
            echo "$NAME_PROMPT"
            read NAME
            echo "New title is $NAME"
            ;;
        $SET_FPS)
            echo "$FPS_PROMPT"
            read FPS
            echo "New FPS is $FPS"
            ;;
        $SET_QUALITY)
            echo "$QUALITY_PROMPT"
            read $QUALITY
            echo "New Quality is $QUALITY"
            ;;
        $SET_DIR)
            echo "$DIR_PROMPT"
            read $DIRECTORY
            echo "New Directory is $DIRECTORY"
            ;;
        $QUIT)
            break
            ;;
        *) echo invalid option;;
    esac
done
###################################################################
# If the export directory doesnt exist already then export
# the RAW files to a new directory and render
#
# If the export directory exists already then render the Timelapse
# Allows the user to define the script variables manually
###################################################################
if [ ! -d "$EXPORT" ]; then
  export
  listFiles
  #if [ ! $JPEG = "false" ]; then
  #    jpegDeflicker
  #fi
  render
  quit
else
  listFiles
  render
  quit
fi
