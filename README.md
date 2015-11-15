songvid
=======

A tool to create a video with a still image and a given audio track

Needs ffmpeg compiled with `--enable-libfdk-aac` and `--enable-nonfree`

Usage
-----

    usage: songvid [-h] image audio
    
    positional arguments:
      image       Image filename
      audio       Audio filename
    
    optional arguments:
      -h, --help  show this help message and exit

Installation
------------

Via `pip`:

    pip3 install songvid

Alternatively:

 * Clone the repository, `cd songvid`
 * Run `python3 setup.py install` or `pip3 install -e`
