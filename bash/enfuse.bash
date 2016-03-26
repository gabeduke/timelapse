#!/bin/bash

# FOCUS STACKING
# TODO Research focus stacking scripts

align_image_stack -a ais_ *.jpg

enfuse -o result.tif ais*.jpg
