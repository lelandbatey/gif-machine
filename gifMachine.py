from __future__ import print_function
import time
from pprint import pprint
import sys
import random
from subprocess import call

# Takes several arugments:
# 
# [1] `youtube_video_link` the http:// link to the youtube video, to be downloaded by youtube-dl.
# [2] `start_time` formatted as "HH:MM:SS"
# [3] `duration` formatted as "SS"

def verify_time(startTime = None):
    
    # Since we need the time format for the beginning to be in the form of
    # "HH:MM:SS" for ffmpeg to work correctly, we make sure it's at the very
    # least in the correct format. However, this is a hacky solution and may
    # mangle input or otherwise return things that are different than the
    # intended input time.
    if not startTime:
        startTime = sys.argv[2]

    startTime = startTime.split(":")

    if len(startTime) != 3: # Not supplied enough arguments
        while len(startTime) < 3:
            startTime.insert(0,"00") # Tacks on a 00 till it's the correct length.

    startTime = ":".join(startTime)
    return startTime

def create_rand_name(nameLength = 6):
    """Generates a random string of lowercase letters and numbers of length 'nameLength'."""

    ourStr = ""
    i = 0
    while i < nameLength:
        if random.randint(0,1): # If we get a 1, we do letters
            ourChar = chr(random.randint(97,122))
            ourStr += ourChar

        else: # we get a 0, we do a number
            ourChar = str(random.randint(1,9))
            ourStr += ourChar
        i += 1

    return ourStr

def main(videoLink=None,startTime=None, endTime = None):

    doneFlag = False

    if len(sys.argv) < 3:
        print("Did not provide enough arguments :/ \n Exiting.")
        doneFlag = True

    if not doneFlag:

        # Verify the start time is in the correct format
        startTime = verify_time(sys.argv[2])

        # If the end time is passed in as an absolute point, verify that as well.
        if ":" in sys.argv[3]:
            endTime = verify_time(sys.argv[3])
        else:
            endTime = sys.argv[3]

        # If that command line argument is a youtube link, then set that as the videoLink
        if "youtube" in sys.argv[1]:
            videoLink = sys.argv[1]

        gifName = create_rand_name() + ".gif"
        

        # Run the actual command
        call(['./videoConverter.sh', videoLink, startTime, endTime, gifName ])

        print("Video has been converted and is: "+gifName)


    


if __name__ == '__main__':
    main()