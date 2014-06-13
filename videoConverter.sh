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

sleep 3

VIDEO_LINK="$1"
START_TIME="$2"
END_TIME="$3"
GIF_NAME="$4"
GIF_WIDTH="$5"
OUTPUT_DIR="$6"

# Takes several arugments:
# 
# 1. `youtube_video_link` the http:// link to the youtube video, to be downloaded by youtube-dl.
# 2. `start_time` formatted as "HH:MM:SS"
# 3. `end_time` formatted as "SS"
# 4. `gif_name` (name of gif)
# 5. `gif_width` width of the gif, in pixels
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

youtube-dl -f 18/17/22 -o "video.mp4" $1

# Layout of how the FFMPEG command needs to look:
#     ffmpeg -i the_video_file.mp4 -ss {start_timestamp} -t {duration} out%04d.png
echo "avconv -i video.mp4 -ss $START_TIME -t $END_TIME out%04d.png"
avconv -loglevel panic -i video.mp4 -ss "$START_TIME" -t "$END_TIME" out%04d.png


# Combines all the frames into one very nicely animated gif.
convert -layers optimize -fuzz 1.5% -delay 4 out*.png -resize "$GIF_WIDTH" anim.gif 


# If the user hasn't passed in an output directory, then set the output
# directory to be the original directory. This is done because this script may
# be used outside of automated environments.
if [ -z "$OUTPUT_DIR" ]; then
	OUTPUT_DIR="$ORIGINAL_DIR"
fi


# Moving our completed gif back to our correct directory, with the correct
# name (if specified).
if [ -n "$GIF_NAME" ]; then
	mv anim.gif $ORIGINAL_DIR$GIF_NAME
else
	mv anim.gif $ORIGINAL_DIR
fi


# Cleaning up

cd $ORIGINAL_DIR
rm -rf $TEMPDIR
echo "Finished converting video to .gif!"
