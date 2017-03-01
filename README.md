## timelapse ##

timelapse is a bash script for compiling timelapses from Canon RAW Images on Linux. It can take 3 parameters which set the Title of the exported .avi file, the FPS and the quality of the final render. When running the script, there will be a menu prompt that allows all of these variables to be adjusted manually.

*Usage*

Add the Canon RAW files to a directory and import into Darktable this will allow DT to create the necessary XMP sidecar files for the script to export the images. You may perform any image adjustments in Darktable you would like and they will be applied to the final export. Then you may just execute timelapse from the image directory for the images to export.

*Installation & Execution*

    chmod +x timelapse.bash
    sudo cp timelapse.bash /usr/bin/timelapse
    cd [image directory]
    timelapse [name] [fps] [quality]


----