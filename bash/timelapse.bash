#!/bin/bash

# Script Parameters
NAME=${1:-rendered}
FPS=${2:-24}
QUALITY=${3:-normal}
DIRECTORY=4:~/Videos/export
# TODO Add JPEG deflickering option
# JPEG=${3:-false}

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
if [ $3 = "high" ]; then
# TODO check syntax & add low quality pass
    LAVCOPTS=$LAVCOPTS+":trell:mbd=2:dc=10"
    fi

# first totals the number of files then exports
# each RAW image using darktable-cli while incrementing
# the counter and comparing to the total variable above
# TODO change CR2 to a RAW Variable
function export() {
TOTAL="$(ls *.CR2 -l | wc -l)"
    for i in $( ls *.CR2 ); do
        darktable-cli $i $i.xmp $DIRECTORY/$i.jpg
        COUNTER=$((COUNTER+1))
        printf "%s/%s\n" "$COUNTER" "$TOTAL"
    done
}

# create file list
function listFiles {
    ls -v export | grep jpg > $DIRECTORY/files.txt
}

# render
function render () {
    cd $DIRECTORY && mencoder -nosound -ovc lavc -lavcopts $3 -o $1.avi -mf type=jpeg:fps=$2 mf://@files.txt -vf scale=1920:1080
    notify-send -t 5000 "Your timelapse has finished rendering and is located at " + $1
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
if [ ! -d "$DIRECTORY" ]; then
  export
  listFiles
  if [ ! $JPEG = "false" ]; then
      jpegDeflicker
  fi
  render $NAME $FPS $LAVCOPTS
  quit
else
  render $NAME $FPS $LAVCOPTS
  quit
fi
