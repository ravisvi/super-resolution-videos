#!/usr/bin/env python3

import os
import video_super_resolver as vsr


def get_videos():
    directory_path = 'videos'
    video_ext = ('avi', 'dat', 'mp4', 'mkv', 'vob')
    videos = []
    files = os.listdir(directory_path)
    for f in files:
        fpath = os.path.join(directory_path, f)
        if(os.path.isfile(fpath)):
            if(fpath.endswith(video_ext)):
                videos.append(f)
    return videos

if __name__ == '__main__':
    
    v = get_videos()
    if(len(v)==0):
        print('No videos found in the videos folder. Please add a video and try again.')
        exit(0)
    
    print('Select a video to super resolve. Enter 1 for the first video.')
    for x in range(1, len(v)+1):
        print(x, '. ', v[x-1])

    choice = int(input())
    print('Selected', v[choice-1])


    vsr.evaluate(v[choice-1])

    # Optional open two vlcs to start at the same time in half windows to show the video. One low res and one hight res.
