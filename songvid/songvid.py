#!/usr/bin/env python
from __future__ import print_function

import argparse
import subprocess
import sys

def create_video(image="", audio=""):
    cmd = ["ffmpeg", "-loop", "1", "-i", image, "-i", audio, "-shortest", "-c:v", "libx264", "-tune", "stillimage", "-c:a", "libfdk_aac", "sv_{}.mp4".format(".".join(audio.split(".")[:-1]))]
    print(cmd)
    outp = subprocess.check_output(cmd)
    print(outp)
    return True

def main():
    parser = argparse.ArgumentParser(prog="songvid")
    parser.add_argument("image", help="Image filename")
    parser.add_argument("audio", help="Audio filename")
    args = parser.parse_args()
    create_video(image=args.image, audio=args.audio)
    return 0


if __name__ == "__main__":
    sys.exit(main())
