# file2wav
File2wav is a python script that allows you to convert any file (of any type) to a wav file. Not too much use from this besides listing to weird sounds or maybe sampling the sounds that come from this program. 


# How-to

Download the `wav.py` file.  Then use the command:
`Python3 wav.py [inputfilename] [outputfilename] [bitrate] [channels] [samplewidth]`

# Arguments
## Bitrate
The bitrate argument allows you to choose the bitrate at which the file saves as. The Higher the number the more "frames" are stored within the file. In this case, the larger the bitrate - the shorter your file will be 
## Channels
The Channel argument allows you to set the number of channels your file will save. For example, a channel argument of 1 will produce a mono sound file while a channel of two will be in stereo 
## Sample width
The Sample width argument set the number of bytes per sample. You will usually keep this at a 1 or 2
