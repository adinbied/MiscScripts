#!/bin/bash
# NOTE: Read commented things to understand what they do as some variables need to be changed!
# This script requires a few things to run. First, it requires youtube-dl, which can be found here: "https://rg3.github.io/youtube-dl/download.html"
# Second, you need a Youtube account with Youtube Red, either free trial or paid. Finally, you need ffmpeg, which can be found here in case it is not already installed: "https://ffmpeg.org/download.html"
cd <save directory> && # Where you want the file
# The below code will download 1080p video and highest quality audio, then merge them together into a .mkv format.
youtube-dl -u <username> -p <password> -f 137+258 <video_URL> # Change variables accordingly, Youtube (Google) account info
# If you want a different quality, use:
# youtube-dl -u <username> -p <password> -F <video_URL>
# which will list the different quality options, then to select options use:
# youtube-dl -u <username> -p <password> -f <video_ID>+<audio_ID> <video_URL>
# Enjoy!
