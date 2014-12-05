#!/bin/bash

# Sets up a variable to track where we were at the start of all this
ORIGINAL_DIR=$(echo $PWD)
ORIGINAL_DIR+="/"

# Sets up temporary directory for the conversion process.
TEMPDIR=$(mktemp -d)

cd $TEMPDIR
echo -e "INVOKED WITH:\n\t$0 $1 $2 $3 $4 $5 $6"
echo "Tempdir: $TEMPDIR"
echo "Original dir: $ORIGINAL_DIR"
#echo "avconv -i video.mp4 -ss $2 -t $3 out%04d.png"

sleep 3
# Takes several arugments:
# 
# 1. `youtube_video_link` the http:// link to the youtube video, to be downloaded by youtube-dl.
# 2. `start_time` formatted as "HH:MM:SS"
# 3. `duration` formatted as "SS"
# 4. `gif_name` the name of the final gif
# 5. `width` as number of pixels
# 6. `output_dir` as a path to a directory
 

# These are required, but the other commands aren't
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

youtube-dl --no-playlist -f 18/17/22 -o "video.mp4" $1

# Layout of how the FFMPEG command needs to look:
#     ffmpeg -i the_video_file.mp4 -ss {start_timestamp} -t {duration} out%04d.png
echo "ffmpeg -i video.mp4 -ss $2 -t $3 out%04d.png"
ffmpeg -loglevel panic -i video.mp4 -ss "$2" -t "$3" out%04d.png
ffmpeg -i out%04d.png -c:v libvpx -b:v 1M -crf 4 anim.webm

OUTPUT_DIR="$6"
mv anim.webm $OUTPUT_DIR$4

cd $ORIGINAL_DIR

rm -rf $TEMPDIR

echo "Finished converting video to .gif!"
