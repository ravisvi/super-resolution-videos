# Super resolve videos
Applying SRGAN technique implemented in https://github.com/zsdonghao/SRGAN on videos to super resolve them.

## Motivation
One of the state of the art techniques at the time to super resolve an image involves the SRGAN technique as described in the [paper](https://arxiv.org/pdf/1609.04802.pdf). We want to investigate the effects of trying this technique on videos to see if we can super resolve them without major distortions.

## Implementation
This repository gives you a framework to choose any video within the videos folder and super reolve it by 4x. Our code works well for most of the videos we have tested. We have added an L1 loss in the training code to get rid of the flickering frames problem found in videos that were super rewsolved using plain SRGANs. 
