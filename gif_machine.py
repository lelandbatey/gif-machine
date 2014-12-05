from __future__ import print_function
from subprocess import call
import random
import os


def verify_time(start_time):
    
    # Since we need the time format for the beginning to be in the form of
    # "HH:MM:SS" for ffmpeg to work correctly, we make sure it's at the very
    # least in the correct format. However, this is a hacky solution and may
    # mangle input or otherwise return things that are different than the
    # intended input time.

    start_time = start_time.split(":")

    if len(start_time) != 3: # Not supplied enough arguments
        while len(start_time) < 3:
            # Tacks on a 00 till it's the correct length.
            start_time.insert(0, "00")

    start_time = ":".join(start_time)
    return start_time

def create_rand_name(length=8):
    """Returns random string of length 'length'.

    String is composed only of lowercase letters and numerals 1 - 9.
    """

    name = ""
    i = 0
    while i < length:
        # If we get a 1, we do letters
        if random.randint(0, 1):
            char = chr(random.randint(97, 122))
            name += char
        # we get a 0, we do a number
        else:
            char = str(random.randint(1, 9))
            name += char
        i += 1

    return name

def calc_seconds(time_arry):
    """Converts time_array into number of seconds.

    Array passed in must be of format ['hh','mm','ss']
    """
    seconds = (int(time_arry[0])*3600) +\
              (int(time_arry[1])*60) +\
              (int(time_arry[2]))
    return seconds

def diff_time(start_time, end_time):
    """Given returns number of seconds between start and end timestamps.

    Timestamps must be of format HH:MM:SS.
    """
    start_time = start_time.split(':')
    end_time = end_time.split(':')

    start_second = calc_seconds(start_time)
    end_seconds = calc_seconds(end_time)

    difference = end_seconds - start_second
    return str(difference)


def build_gif(video_link=None, start_time=None, end_time=None,
              output_directory="", width=None):
    """Builds the specified gif, returning the name of that gif."""

    if not width:
        width = "150"

    start_time = verify_time(start_time)
    gif_name = create_rand_name() + ".webm"

    print("video_link:", video_link)
    print("start_time:", start_time)
    print("end_time:", end_time)
    print("output_directory:", output_directory)
    print("width:", width)
    
    print('./videoConverter.sh', video_link, start_time, end_time,
          gif_name, width, output_directory)
    
    # Run the actual command
    call(['./videoConverter.sh', video_link, start_time, end_time,
          gif_name, width, output_directory], cwd=os.getcwd())

    print("Video has been converted and is:", gif_name)
    return gif_name
    


if __name__ == '__main__':
    build_gif()
