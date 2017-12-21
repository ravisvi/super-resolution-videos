# Super resolve videos
Applying SRGAN technique implemented in https://github.com/zsdonghao/SRGAN on videos to super resolve them.

## Motivation
One of the state of the art techniques at the time to super resolve an image involves the SRGAN technique as described in the [paper](https://arxiv.org/pdf/1609.04802.pdf). We want to investigate the effects of trying this technique on videos to see if we can super resolve them without major distortions.

## Implementation
This repository gives you a framework to choose any video within the videos folder and super reolve it by 4x. Our code works well for most of the videos we have tested. We have added an L1 loss in the training code to get rid of the flickering frames problem found in videos that were super rewsolved using plain SRGANs. 

### Running the script
Provided that the repository has access to the trained model, the entry point to this project would be via the supervideo.py file. 
This files lists the video files present in the videos folder. The repository as is, is void of any videos. So go ahead and place any number of videos in this folder.

1. To execute this, please run `python supervideo.py`
2. Select the desired video from the list.
3. Once the operation is successful the video will be present in the same folder with _srgan suffix.

Please contact [@ravisvi](https://github.com/ravisvi) or [@kevinjoseph1995](https://github.com/kevinjoseph1995) if you need the trained model. 

### Dependencies
1. A python environment
2. Working TensorFlow installation
3. Working TensorLayer installation



