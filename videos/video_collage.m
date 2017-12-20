clc;
clear;
close all;
v1_read = VideoReader('football_lq.mp4');
v2_read = VideoReader('football_lq_srgan.mp4');
v3_read = VideoReader('football_lq_srgan1.mp4');
i=1
while hasFrame(v1_read) 
    frame1 = readFrame(v1_read);
    frame1 =imresize(frame1,0.5);
    frame1 =imresize(frame1,8);
    frame2 = readFrame(v2_read);
    frame3 = readFrame(v3_read)+randi([-5,20]);
    if i>927 && i<=930
        imwrite([frame1;frame2;frame3],strcat('C:\Users\kevin\Documents\GitHub\super-resolution-videos\videos\Image_Dump\',num2str(i),'.png'))
    end
    i=i+1
    if i>930
        break
    end
end