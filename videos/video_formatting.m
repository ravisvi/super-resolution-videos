clc;
clear;
close all;
v_read = VideoReader('bugs_hq.mp4');
v_write=VideoWriter('bugs_lq', 'MPEG-4');
v_write.FrameRate=v_read.FrameRate;
open(v_write)
i=1;
while hasFrame(v_read)
    frame = readFrame(v_read);
    resized_frame=imresize(frame,0.25);
    writeVideo(v_write,resized_frame);    
    i=i+1
end
close(v_write)