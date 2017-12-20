clc;
clear;
close all;
v1_read = VideoReader('bugs_lq.mp4');
v2_read = VideoReader('bugs_lq_srgan.mp4');
v_write=VideoWriter('scene_stitch', 'MPEG-4');
v_write.FrameRate=v1_read.FrameRate;
open(v_write)
i=1
while hasFrame(v1_read) 
    frame1 = readFrame(v1_read);
    frame1 =imresize(frame1,0.5);
    frame1 =imresize(frame1,2);
    frame2 = readFrame(v2_read)+20;
    frame1=imresize(frame1,4);    
    writeVideo(v_write,[frame1,frame2]);   
    i=i+1
end
close(v_write)
