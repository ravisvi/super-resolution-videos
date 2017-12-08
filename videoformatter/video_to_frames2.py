import skvideo.io
import os
import scipy
import collections

class VideoReader:
    def __init__(self):
        os.chdir("../")
        self.project_directory=os.getcwd()        
    def read_video(self):
        video_filepath=self. project_directory+'\\videos\\video_hq.mp4'
        print (video_filepath)
        videogen = skvideo.io.vreader(video_filepath)
        metadata = skvideo.io.ffprobe(video_filepath)
        metadata=metadata['video']
        H=metadata['@height']
        W=metadata['@width']
        fps=metadata['@r_frame_rate']
        print (H,W,fps)
        # writer = skvideo.io.FFmpegWriter("outputvideo.mp4",inputdict={'-r': '30000/1001' },outputdict={'-r': '30000/1001'})
        # print (metadata)
        # for frame in videogen:
            # writer.writeFrame(frame)
        # writer.close()    
            
    
        
 
        
vr=VideoReader()
vr.read_video()
