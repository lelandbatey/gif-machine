#!/bin/bash

# Sets up a variable to track where we were at the start of all this
ORIGINAL_DIR=$(echo $PWD)
ORIGINAL_DIR+="/"

# Sets up temporary directory for the conversion process.
TEMPDIR=$(mktemp -d)

cd $TEMPDIR
echo -e "INVOKED WITH:\n\t$0 $1 $2 $3 $4 $5"
echo "Tempdir: $TEMPDIR"
echo "Original dir: $ORIGINAL_DIR"
#echo "avconv -i video.mp4 -ss $2 -t $3 out%04d.png"

sleep 3
# Takes several arugments:
# 
# 1. `youtube_video_link` the http:// link to the youtube video, to be downloaded by youtube-dl.
# 2. `start_time` formatted as "HH:MM:SS"
# 3. `duration` formatted as "SS"
 
if [ -z "$1" ]; then
	echo "You didn't provide a first argument -- Exiting."
	exit
else
	if [ -z "$2" ]; then
		echo "You didn't provide a second argument -- Exiting."
		exit
	else
		if [ -z "$3" ]; then
			echo "No third argument -- Exiting."
			exit
		fi
	fi
fi
# Done verifying arguments

# Downloads the video file:
# youtube-dl -f 34/35/18/6 -o "video.mp4" $1

youtube-dl -f 18/17/22 -o "video.mp4" $1

# Layout of how the FFMPEG command needs to look:
#     ffmpeg -i the_video_file.mp4 -ss {start_timestamp} -t {duration} out%04d.png
echo "avconv -i video.mp4 -ss $2 -t $3 out%04d.png"
avconv -loglevel panic -i video.mp4 -ss $2 -t $3 out%04d.png


convert -delay 4 out*.png -resize "$5" anim.gif # Combines all the frames into one very nicely animated gif.
#convert -layers Optimize anim.gif optimized_output.gif # Optimizes the gif using imagemagick

# vvvvv Cleans up the leftovers
rm out*
rm anim.gif 

# Moving our completed gif back to our correct directory

if [ -n "$4" ]; then
	mv optimized_output.gif $ORIGINAL_DIR$4
else
	mv optimized_output.gif $ORIGINAL_DIR
fi

cd $ORIGINAL_DIR

rm -rf $TEMPDIR

echo "Finished converting video to .gif!"
