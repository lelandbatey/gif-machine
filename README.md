Gif Machine
===========

Tiny web app for automaticall converting Youtube videos into animated .gifs.

### [DEMO](http://nacr.us/gif)

Requirements
------------

    - FFMpeg (`sudo apt-get install ffmpeg`)
    - ImageMagick (`sudo apt-get install imagemagick`)
    - Flask (`pip install Flask`)
    - youtube_dl (`pip install youtube_dl`)

Notes
-----

This currently doesn't do anything fancy like upload to external sites (such as imgur.com). For now it relies on hosting via the server itself.

Because this is a single threaded app, I recommend you use Gunicorn (or anything like it) to give you some kind of basic concurrency.
