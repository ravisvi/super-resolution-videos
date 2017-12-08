import imageio
import os
import scipy


class VideoReader:
    def __init__(self):
        os.chdir("../")
        self.project_directory=os.getcwd()        
    def read_video(self):
        video_filepath=self. project_directory+'\\videos\\video_hq.mp4'
        print video_filepath
        reader = imageio.get_reader(video_filepath)
        for i, frame in enumerate(reader):
            self.writeFrame(i,frame)
    def writeFrame(self,i,frame):
        image_path=self. project_directory+'\\images\\hq_frames\\'+str(i)+'.png'
        scipy.misc.toimage(frame,channel_axis=2).save(image_path)
 
        
vr=VideoReader()
vr.read_video()
vr.writeFrame()