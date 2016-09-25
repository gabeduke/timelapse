
## Miscellanious Timelapse Scripts ##

*RAW*

    cp /usr/bin/timelapse.py ./timelapse.py
    chmod +x timelapse.py
    python timelapse.py -i /directory -o jpg -r

*JPEG*

1. Export Edited Darktable images to directory
2. Deflicker Jpegs
3. Navigate to JPEG dir
`cp /usr/bin/timelapse-deflicker.pl ./timelapse-deflicker.pl`
`./timelapse-deflicker.pl -v`

* to install dependencies
`(cpan module::foo)`

*Motion Blur*

    cd Deflickered
    mogrify -verbose -limit memory 8192 *.jpg -delay 10 -morph 5

*Compile Jpegs to AVI*

    cd Deflickered
    ls -1v | grep jpg > files.txt && mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=21600000 -o 01_rendered.avi -mf type=jpeg:fp	s=24 mf://@files.txt -vf scale=1920:1080

### Setup ###

*JPEG Deflicker Script*

* Perl/deflicker.pl
* Save the above Perl script to /usr/bin/timelapse-deflicker.pl
`sudo cp /usr/bin/timelapse-deflicker.pl ./timelapse-deflicker.pl`
`sudo chmod +x timelapse-deflicker.pl`

----


*RAW Deflicker Script*

* Python/timelapse.md
* Save the above Python script to the /usr/bin/timelapse.py
* Install dependencies
`sudo apt-get install ufraw`
`sudo apt-get install python-imaging-tk`
`sudo apt-get install python-numpy python-scipy python-matplotlib`
* Navigate to the Dir w/ raw files
`cp ~/bin/timelapse.py ./timelapse.py`
`chmod +x timelapse.py`
`python timelapse.py -i /directory -o jpg -r`

----

*AVI Export Script*
* Nav to JPEG Dir

`ls -1v | grep jpg > files.txt`
`mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=21600000 -o rendered.avi -mf type=jpeg:fps=24 mf://@files.txt -vf scale=1920:1080`

*Photography HDR Stack*

    align_image_stack -C -a aligned. *.tif
    enfuse -o hdr.tif --saturation-weight=0 aligned*

