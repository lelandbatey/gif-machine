GifMachine Notes
================

For ffmpeg to go to the correct position, it must be passed the start time as "hh:mm:ss". It must be passed in like this EXACTLY. Anything else will break stuff. However, it can actually also take just the total number of seconds into the video (as "seconds") to denote where to start.

The duration of the operation, denoted with the `-t` parameter, can be in either "seconds" format or it can be in the "HH:MM:SS" format, either will work.