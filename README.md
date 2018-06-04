# Super resolve videos
Applying SRGAN technique implemented in https://github.com/zsdonghao/SRGAN on videos to super resolve them.
You can find some of our results here- https://www.youtube.com/watch?v=8OY8HFGsbKM .
With various modification to the loss methods one can obtain results which match their goals.

## Motivation
One of the state of the art techniques at the time of writing, to super resolve an image involves the SRGAN technique as described in the [paper](https://arxiv.org/pdf/1609.04802.pdf). We investigated the effects of trying this technique on videos, and observed that we can super resolve them without major distortions, though some changes to the loss functions were necessary to remove certain flickering effects.


## Implementation
This repository gives you a framework to choose any video within the videos folder and super reolve it by *4x*. Our code works well for most of the videos we have tested. We have added an L1 loss in the training code to get rid of the flickering frames problem found in videos that were super rewsolved using plain SRGANs. 

NOTE: The trained models are present in the folder Generator_Models. 
1. g_srgan.npz: trained model obtained from the original paper without the loss modifications.
2. g_srgan_L1.npz: trained model with L1 loss to reduce the flickering effect.

### Running the script
Provided that the repository has access to the trained model, the entry point to this project would be via the **supervideo.py** file. 
This files lists the video files present in the videos folder. The repository as is, is void of any videos. So go ahead and place any number of videos in this folder.

1. To execute this, please run `python supervideo.py`
2. Select the desired video from the list.
3. Once the operation is successful the video will be present in the same folder with _srgan suffix.

### Dependencies
1. Python environment
2. Working TensorFlow installation
3. Working TensorLayer installation
4. Python skvideo package
5. ffmpeg tool

## FAQs
### 1. Getting memory errors
Reduce the resolution of the input video. As this code tries to super-resolve the video by 4x, if one tries to super resolve 1080p video, one needs video card memory that can handle 1080x4 pixels. 
**Sometimes**, a video might have a high resolution theoretically, but may just contain noise/ pixelated information. Reducing the resolution, reduces the file size without noticeable quality degradation.
### 2. ffmpeg tool not found. Please have download all the necessary dependencies.
Please install ffmpeg tool/ any other tools that were not found.
### 3. How do I train my model?
We have not included the code for training the models in this repository. We used https://github.com/tensorlayer/srgan/blob/master/main.py, to train our models as well. Please star their repository if you find this technique useful. :)
### 4. I have trained my model, how do I use it?
Once you have a trained model, go ahead and place it in the Generator_Models folder. Then go [here (line 65)](https://github.com/ravisvi/super-resolution-videos/blob/f70e9e8f2f092497f45f3e040475e1377feff4a8/video_super_resolver.py#L65) and put your model's name instead of the current "g_srgan.npz."
You are all set to super resolve a video using this model now.
